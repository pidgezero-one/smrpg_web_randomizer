from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2119_set_short_0',
        "command": 'set_short',
        "args": [0x7000, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2119_clear_bit_1',
        "command": 'clear_bit',
        "args": [0x708a, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2119_start_loop_n_times_2',
        "command": 'start_loop_n_times',
        "args": [19],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2119_pause_3',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2119_set_7000_to_tapped_button_4',
        "command": 'set_7000_to_tapped_button',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2119_jmp_if_7000_all_bits_clear_5',
        "command": 'jmp_if_7000_all_bits_clear',
        "args": [[7], 'EVENT_2119_end_loop_7'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2119_set_bit_6',
        "command": 'set_bit',
        "args": [0x708a, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2119_end_loop_7',
        "command": 'end_loop',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2119_jmp_if_bit_set_8',
        "command": 'jmp_if_bit_set',
        "args": [0x708a, 7, 'EVENT_2120_stop_music_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2119_ret_9',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
