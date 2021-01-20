from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_703_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7090, 4, 'EVENT_703_open_location_5'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_703_set_bit_1',
        "command": 'set_bit',
        "args": [0x7090, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_703_run_event_sequence_2',
        "command": 'run_event_sequence',
        "args": [EventSequences._16_RUN_WORLD_MAP_EVENT_SEQUENCE, OverworldSequences._01_MARIO_RETURNS_TO_MK],
        "subscript": []
    },
    {
        "identifier": 'EVENT_703_enter_area_3',
        "command": 'enter_area',
        "args": [Rooms._191_MUSHROOM_KINGDOM_OUTSIDE, RadialDirections.NORTHWEST, 21, 122, 2, [_0x68Flags.RUN_ENTRANCE_EVENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_703_ret_4',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_703_open_location_5',
        "command": 'open_location',
        "args": [Locations._028_MARRYMORE, [6, 7]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_703_ret_6',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
