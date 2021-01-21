from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1915_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'EVENT_1915_ret_7']
    },
    {
        "identifier": 'EVENT_1915_set_bit_1',
        "command": 'set_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_1915_set_short_2',
        "command": 'set_short',
        "args": [0x7026, 0x0001]
    },
    {
        "identifier": 'EVENT_1915_clear_bit_3',
        "command": 'clear_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'EVENT_1915_clear_bit_4',
        "command": 'clear_bit',
        "args": [0x7043, 2]
    },
    {
        "identifier": 'EVENT_1915_clear_bit_5',
        "command": 'clear_bit',
        "args": [0x7043, 3]
    },
    {
        "identifier": 'EVENT_1915_clear_bit_6',
        "command": 'clear_bit',
        "args": [0x7043, 4]
    },
    {
        "identifier": 'EVENT_1915_ret_7',
        "command": 'ret'
    }
]
