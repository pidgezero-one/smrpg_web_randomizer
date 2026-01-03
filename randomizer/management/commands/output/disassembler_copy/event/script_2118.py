
from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2118_clear_bit_0',
        "command": 'clear_bit',
        "args": [0x708a, 7]
    },
    {
        "identifier": 'EVENT_2118_set_short_1',
        "command": 'set_short',
        "args": [0x7000, 0x0000]
    },
    {
        "identifier": 'EVENT_2118_start_loop_n_times_2',
        "command": 'start_loop_n_times',
        "args": [29]
    },
    {
        "identifier": 'EVENT_2118_pause_3',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_2118_set_7000_to_tapped_button_4',
        "command": 'set_7000_to_tapped_button'
    },
    {
        "identifier": 'EVENT_2118_jmp_if_7000_all_bits_clear_5',
        "command": 'jmp_if_7000_all_bits_clear',
        "args": [[7], 'EVENT_2118_end_loop_7']
    },
    {
        "identifier": 'EVENT_2118_set_bit_6',
        "command": 'set_bit',
        "args": [0x708a, 7]
    },
    {
        "identifier": 'EVENT_2118_end_loop_7',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_2118_jmp_if_bit_clear_8',
        "command": 'jmp_if_bit_clear',
        "args": [0x708a, 7, 'EVENT_2120_stop_music_0']
    },
    {
        "identifier": 'EVENT_2118_set_short_9',
        "command": 'set_short',
        "args": [0x7000, 0x0000]
    },
    {
        "identifier": 'EVENT_2118_ret_10',
        "command": 'ret'
    }
]
