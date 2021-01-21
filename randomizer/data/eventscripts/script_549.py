from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_549_enable_controls_until_return_0',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.X, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]]
    },
    {
        "identifier": 'EVENT_549_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 6, 'EVENT_256_ret_0']
    },
    {
        "identifier": 'EVENT_549_set_bit_2',
        "command": 'set_bit',
        "args": [0x7044, 6]
    },
    {
        "identifier": 'EVENT_549_set_bit_3',
        "command": 'set_bit',
        "args": [0x7044, 2]
    },
    {
        "identifier": 'EVENT_549_ret_4',
        "command": 'ret'
    }
]
