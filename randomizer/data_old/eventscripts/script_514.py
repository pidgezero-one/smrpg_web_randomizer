
from randomizer.helpers.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.helpers.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_514_jmp_if_bit_set_28',
        "command": 'jmp_if_bit_set',
        "args": [0x7085, 7, 'EVENT_514_gaz_Normal']
    },
    {
        "identifier": 'EVENT_514_set_bit_29',
        "command": 'set_bit',
        "args": [0x7085, 7]
    },
    {
        "identifier": 'EVENT_514_gaz_grant',
        "command": 'jmp_to_event',
        "args": [178]
    },
    {
        "identifier": 'EVENT_514_gaz_Normal',
        "command": 'jmp_to_event',
        "args": [516]
    },
]
