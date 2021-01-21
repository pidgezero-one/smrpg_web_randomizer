from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2410_clear_bit_0',
        "command": 'clear_bit',
        "args": [0x7046, 7]
    },
    {
        "identifier": 'EVENT_2410_clear_bit_1',
        "command": 'clear_bit',
        "args": [0x7046, 5]
    },
    {
        "identifier": 'EVENT_2410_clear_bit_2',
        "command": 'clear_bit',
        "args": [0x7046, 6]
    },
    {
        "identifier": 'EVENT_2410_set_bit_3',
        "command": 'set_bit',
        "args": [0x7045, 5]
    },
    {
        "identifier": 'EVENT_2410_jmp_4',
        "command": 'jmp',
        "args": ['EVENT_2416_set_bit_0']
    }
]
