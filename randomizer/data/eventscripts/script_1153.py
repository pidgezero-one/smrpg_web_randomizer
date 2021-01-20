from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1153_jmp_if_bit_clear_0',
        "command": 'jmp_if_bit_clear',
        "args": [0x7086, 6, 'EVENT_1153_jmp_if_bit_set_4'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1153_jmp_1',
        "command": 'jmp',
        "args": ['EVENT_1153_jmp_if_bit_set_4'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1153_remove_from_current_level_2',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1153_remove_from_current_level_3',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1153_jmp_if_bit_set_4',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 7, 'EVENT_1153_run_event_as_subroutine_7'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1153_fade_in_from_black_async_5',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1153_ret_6',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1153_run_event_as_subroutine_7',
        "command": 'run_event_as_subroutine',
        "args": [81],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1153_ret_8',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]