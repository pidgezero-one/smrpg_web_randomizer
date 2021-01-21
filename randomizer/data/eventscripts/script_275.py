from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_275_enable_controls_until_return_0',
        "command": 'enable_controls_until_return',
        "args": [[]]
    },
    {
        "identifier": 'EVENT_275_start_loop_n_times_1',
        "command": 'start_loop_n_times',
        "args": [127]
    },
    {
        "identifier": 'EVENT_275_pause_2',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_275_set_7000_to_tapped_button_3',
        "command": 'set_7000_to_tapped_button'
    },
    {
        "identifier": 'EVENT_275_jmp_if_7000_any_bits_set_4',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[7], 'EVENT_275_set_9']
    },
    {
        "identifier": 'EVENT_275_end_loop_5',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_275_set_6',
        "command": 'set',
        "args": [0x7000, 2]
    },
    {
        "identifier": 'EVENT_275_enable_controls_until_return_7',
        "command": 'enable_controls_until_return',
        "args": [[]]
    },
    {
        "identifier": 'EVENT_275_ret_8',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_275_set_9',
        "command": 'set',
        "args": [0x7000, 0]
    },
    {
        "identifier": 'EVENT_275_enable_controls_until_return_10',
        "command": 'enable_controls_until_return',
        "args": [[]]
    },
    {
        "identifier": 'EVENT_275_ret_11',
        "command": 'ret'
    }
]
