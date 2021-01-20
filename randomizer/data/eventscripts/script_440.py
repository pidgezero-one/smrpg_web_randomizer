from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_440_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7040, 0, 'EVENT_440_reset_and_choose_game_5'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_440_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7040, 1, 'EVENT_440_ret_7'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_440_remove_object_at_70A8_from_current_level_2',
        "command": 'remove_object_at_70A8_from_current_level',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_440_remove_from_current_level_3',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.MEM_70A8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_440_ret_4',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_440_reset_and_choose_game_5',
        "command": 'reset_and_choose_game',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_440_end_all_6',
        "command": 'end_all',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_440_ret_7',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
