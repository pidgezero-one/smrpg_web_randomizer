from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1810_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7094, 6, 'EVENT_1810_jmp_to_event_2'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1810_apply_solidity_mod_1',
        "command": 'apply_solidity_mod',
        "args": [Rooms._422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM, 1, [_0x6BFlags.PERMANENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1810_jmp_to_event_2',
        "command": 'jmp_to_event',
        "args": [15],
        "subscript": []
    }
]
