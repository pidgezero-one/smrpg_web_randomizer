from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_530_clear_bit_0',
        "command": 'clear_bit',
        "args": [0x7044, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_530_clear_bit_1',
        "command": 'clear_bit',
        "args": [0x7044, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_530_clear_bit_2',
        "command": 'clear_bit',
        "args": [0x7044, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_530_clear_bit_3',
        "command": 'clear_bit',
        "args": [0x7044, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_530_pause_4',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_530_jmp_if_bit_set_5',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 6, 'EVENT_530_run_event_as_subroutine_7'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_530_jmp_6',
        "command": 'jmp',
        "args": ['EVENT_530_pause_4'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_530_run_event_as_subroutine_7',
        "command": 'run_event_as_subroutine',
        "args": [548],
        "subscript": []
    },
    {
        "identifier": 'EVENT_530_jmp_if_bit_set_8',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 5, 'EVENT_530_jmp_if_random_above_128_11'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_530_pause_9',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_530_jmp_10',
        "command": 'jmp',
        "args": ['EVENT_530_jmp_if_bit_set_8'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_530_jmp_if_random_above_128_11',
        "command": 'jmp_if_random_above_128',
        "args": ['EVENT_530_pause_14'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_530_pause_12',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_530_jmp_13',
        "command": 'jmp',
        "args": ['EVENT_530_clear_bit_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_530_pause_14',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_530_jmp_15',
        "command": 'jmp',
        "args": ['EVENT_530_clear_bit_0'],
        "subscript": []
    },
]
