from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_558_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7083, 6, 'EVENT_558_enter_area_3'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_558_enter_area_1',
        "command": 'enter_area',
        "args": [Rooms._083_ROSE_TOWN_DURING_BOWYER_OUTSIDE, RadialDirections.SOUTHWEST, 20, 47, 1, [_0x68Flags.RUN_ENTRANCE_EVENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_558_ret_2',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_558_enter_area_3',
        "command": 'enter_area',
        "args": [Rooms._084_ROSE_TOWN_OUTSIDE, RadialDirections.SOUTHWEST, 20, 47, 1, [_0x68Flags.RUN_ENTRANCE_EVENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_558_ret_4',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
