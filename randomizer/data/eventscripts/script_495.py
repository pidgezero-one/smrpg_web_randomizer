from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_495_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 0, 'EVENT_256_ret_0']
    },
    {
        "identifier": 'EVENT_495_set_bit_1',
        "command": 'set_bit',
        "args": [0x7044, 0]
    },
    {
        "identifier": 'EVENT_495_clear_bit_2',
        "command": 'clear_bit',
        "args": [0x7043, 7]
    },
    {
        "identifier": 'EVENT_495_clear_bit_3',
        "command": 'clear_bit',
        "args": [0x7044, 1]
    },
    {
        "identifier": 'EVENT_495_jmp_if_bit_set_4',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 5, 'EVENT_495_clear_bit_8']
    },
    {
        "identifier": 'EVENT_495_clear_bit_5',
        "command": 'clear_bit',
        "args": [0x7044, 4]
    },
    {
        "identifier": 'EVENT_495_set_bit_6',
        "command": 'set_bit',
        "args": [0x7044, 5]
    },
    {
        "identifier": 'EVENT_495_ret_7',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_495_clear_bit_8',
        "command": 'clear_bit',
        "args": [0x7044, 5]
    },
    {
        "identifier": 'EVENT_495_set_bit_9',
        "command": 'set_bit',
        "args": [0x7044, 4]
    },
    {
        "identifier": 'EVENT_495_ret_10',
        "command": 'ret'
    }
]
