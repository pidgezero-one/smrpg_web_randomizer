from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_753_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 0, 'EVENT_256_ret_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_753_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 5, 'EVENT_256_ret_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_753_jmp_2',
        "command": 'jmp',
        "args": ['EVENT_289_set_7000_to_current_level_0'],
        "subscript": []
    }
]
