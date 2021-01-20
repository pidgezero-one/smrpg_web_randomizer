from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_272_pause_0',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_272_set_7000_to_tapped_button_1',
        "command": 'set_7000_to_tapped_button',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_272_jmp_if_7000_any_bits_set_2',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[5], 'EVENT_272_ret_4'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_272_jmp_3',
        "command": 'jmp',
        "args": ['EVENT_272_pause_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_272_ret_4',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
