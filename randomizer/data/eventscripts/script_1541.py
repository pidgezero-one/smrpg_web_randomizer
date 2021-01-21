from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1541_clear_bit_0',
        "command": 'clear_bit',
        "args": [0x707b, 4]
    },
    {
        "identifier": 'EVENT_1541_clear_bit_1',
        "command": 'clear_bit',
        "args": [0x707b, 5]
    },
    {
        "identifier": 'EVENT_1541_pause_2',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1541_set_7000_to_tapped_button_3',
        "command": 'set_7000_to_tapped_button'
    },
    {
        "identifier": 'EVENT_1541_jmp_if_7000_all_bits_clear_4',
        "command": 'jmp_if_7000_all_bits_clear',
        "args": [[4, 5, 6, 7], 'EVENT_1541_pause_2']
    },
    {
        "identifier": 'EVENT_1541_jmp_if_7000_any_bits_set_5',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[7], 'EVENT_1541_set_bit_8']
    },
    {
        "identifier": 'EVENT_1541_jmp_if_7000_any_bits_set_6',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[5], 'EVENT_1541_set_bit_10']
    },
    {
        "identifier": 'EVENT_1541_ret_7',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1541_set_bit_8',
        "command": 'set_bit',
        "args": [0x707b, 4]
    },
    {
        "identifier": 'EVENT_1541_ret_9',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1541_set_bit_10',
        "command": 'set_bit',
        "args": [0x707b, 5]
    },
    {
        "identifier": 'EVENT_1541_ret_11',
        "command": 'ret'
    }
]
