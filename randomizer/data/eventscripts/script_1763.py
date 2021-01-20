from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1763_jmp_if_object_not_in_level_0',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_6, Rooms._318_LANDS_END_DESERT_AREA_02, 'EVENT_1763_run_event_as_subroutine_3'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1763_set_1',
        "command": 'set',
        "args": [0x70a8, 26],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1763_jmp_2',
        "command": 'jmp',
        "args": ['EVENT_1887_jmp_if_bit_set_4'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1763_run_event_as_subroutine_3',
        "command": 'run_event_as_subroutine',
        "args": [1544],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1763_enter_area_4',
        "command": 'enter_area',
        "args": [Rooms._404_LANDS_END_DESERT_AREA_04, RadialDirections.SOUTH, 22, 102, 0, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1763_run_event_as_subroutine_5',
        "command": 'run_event_as_subroutine',
        "args": [1844],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1763_set_6',
        "command": 'set',
        "args": [0x70a8, 21],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1763_run_event_as_subroutine_7',
        "command": 'run_event_as_subroutine',
        "args": [1545],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1763_jmp_to_event_8',
        "command": 'jmp_to_event',
        "args": [1786],
        "subscript": []
    },
]