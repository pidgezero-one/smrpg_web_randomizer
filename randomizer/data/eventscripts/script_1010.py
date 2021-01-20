from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1010_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7040, 0, 'EVENT_287_reset_and_choose_game_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1010_set_short_mem_1',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70a9],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1010_set_short_mem_2',
        "command": 'set_short_mem',
        "args": [0x70a8, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1010_remove_object_at_70A8_from_current_level_3',
        "command": 'remove_object_at_70A8_from_current_level',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1010_remove_from_current_level_4',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.MEM_70A8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1010_jmp_if_bit_set_5',
        "command": 'jmp_if_bit_set',
        "args": [0x704a, 2, 'EVENT_1010_clear_bit_7'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1010_fade_in_from_black_async_6',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1010_clear_bit_7',
        "command": 'clear_bit',
        "args": [0x704a, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1010_ret_8',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
