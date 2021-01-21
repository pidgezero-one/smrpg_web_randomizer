from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_494_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 7, 'EVENT_256_ret_0']
    },
    {
        "identifier": 'EVENT_494_set_bit_1',
        "command": 'set_bit',
        "args": [0x7043, 7]
    },
    {
        "identifier": 'EVENT_494_clear_bit_2',
        "command": 'clear_bit',
        "args": [0x7044, 0]
    },
    {
        "identifier": 'EVENT_494_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 4, 'EVENT_494_clear_bit_7']
    },
    {
        "identifier": 'EVENT_494_clear_bit_4',
        "command": 'clear_bit',
        "args": [0x7044, 3]
    },
    {
        "identifier": 'EVENT_494_set_bit_5',
        "command": 'set_bit',
        "args": [0x7044, 4]
    },
    {
        "identifier": 'EVENT_494_ret_6',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_494_clear_bit_7',
        "command": 'clear_bit',
        "args": [0x7044, 4]
    },
    {
        "identifier": 'EVENT_494_set_bit_8',
        "command": 'set_bit',
        "args": [0x7044, 3]
    },
    {
        "identifier": 'EVENT_494_ret_9',
        "command": 'ret'
    }
]
