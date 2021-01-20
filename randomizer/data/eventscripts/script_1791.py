from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1791_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7050, 4, 'EVENT_1791_jmp_to_event_4'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1791_set_bit_1',
        "command": 'set_bit',
        "args": [0x7050, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1791_set_short_2',
        "command": 'set_short',
        "args": [0x701c, 0x005a],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1791_run_background_event_with_pause_return_on_exit_3',
        "command": 'run_background_event_with_pause_return_on_exit',
        "args": [1788, 0x701c, [12, 13]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1791_jmp_to_event_4',
        "command": 'jmp_to_event',
        "args": [15],
        "subscript": []
    }
]
