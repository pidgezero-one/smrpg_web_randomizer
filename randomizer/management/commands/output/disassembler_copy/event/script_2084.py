
from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2084_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7089, 5, 'EVENT_2084_ret_7']
    },
    {
        "identifier": 'EVENT_2084_jmp_if_bit_clear_1',
        "command": 'jmp_if_bit_clear',
        "args": [0x7089, 3, 'EVENT_2084_ret_7']
    },
    {
        "identifier": 'EVENT_2084_set_2',
        "command": 'set',
        "args": [0x70a7, 162]
    },
    {
        "identifier": 'EVENT_2084_set_3',
        "command": 'set',
        "args": [0x7000, 3005]
    },
    {
        "identifier": 'EVENT_2084_run_event_as_subroutine_4',
        "command": 'run_event_as_subroutine',
        "args": [3828]
    },
    {
        "identifier": 'EVENT_2084_set_bit_5',
        "command": 'set_bit',
        "args": [0x7089, 5]
    },
    {
        "identifier": 'EVENT_2084_ret_6',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2084_ret_7',
        "command": 'ret'
    }
]
