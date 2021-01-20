from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3796_set_7000_to_tapped_button_0',
        "command": 'set_7000_to_tapped_button',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3796_pause_1',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3796_jmp_if_7000_any_bits_set_2',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[7], 'EVENT_3796_run_event_at_return_5'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3796_jmp_if_7000_any_bits_set_3',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[5], 'EVENT_3796_run_event_at_return_7'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3796_jmp_to_event_4',
        "command": 'jmp_to_event',
        "args": [3796],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3796_run_event_at_return_5',
        "command": 'run_event_at_return',
        "args": [3802],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3796_ret_6',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3796_run_event_at_return_7',
        "command": 'run_event_at_return',
        "args": [3795],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3796_ret_8',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
