from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_492_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 3, 'EVENT_256_ret_0']
    },
    {
        "identifier": 'EVENT_492_set_bit_1',
        "command": 'set_bit',
        "args": [0x7044, 3]
    },
    {
        "identifier": 'EVENT_492_ret_2',
        "command": 'ret'
    }
]
