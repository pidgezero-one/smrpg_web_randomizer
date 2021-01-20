from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1684_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x704e, 7, 'EVENT_1684_enter_area_3'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1684_enter_area_1',
        "command": 'enter_area',
        "args": [Rooms._422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM, RadialDirections.SOUTHEAST, 1, 116, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1684_ret_2',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1684_enter_area_3',
        "command": 'enter_area',
        "args": [Rooms._426_BELOME_TEMPLE_AREA_07_PIPE_TO_BELOMES_ROOM, RadialDirections.SOUTHEAST, 26, 11, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1684_ret_4',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
