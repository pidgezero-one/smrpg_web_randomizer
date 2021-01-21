from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_266_enable_controls_until_return_0',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.X, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]]
    },
    {
        "identifier": 'EVENT_266_set_short_mem_1',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70bb]
    },
    {
        "identifier": 'EVENT_266_mem_compare_2',
        "command": 'mem_compare',
        "args": [0x7000, 0x702e]
    },
    {
        "identifier": 'EVENT_266_jmp_if_comparison_result_is_greater_or_equal_3',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_266_clear_bit_6']
    },
    {
        "identifier": 'EVENT_266_set_bit_4',
        "command": 'set_bit',
        "args": [0x7044, 0]
    },
    {
        "identifier": 'EVENT_266_jmp_5',
        "command": 'jmp',
        "args": ['EVENT_256_ret_0']
    },
    {
        "identifier": 'EVENT_266_clear_bit_6',
        "command": 'clear_bit',
        "args": [0x7044, 0]
    },
    {
        "identifier": 'EVENT_266_ret_7',
        "command": 'ret'
    }
]
