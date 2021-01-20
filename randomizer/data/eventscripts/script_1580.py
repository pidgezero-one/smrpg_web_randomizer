from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1580_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 6, 'EVENT_1580_ret_9'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1580_clear_bit_1',
        "command": 'clear_bit',
        "args": [0x7044, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1580_clear_bit_2',
        "command": 'clear_bit',
        "args": [0x7043, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1580_set_bit_3',
        "command": 'set_bit',
        "args": [0x7043, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1580_jmp_if_var_equals_short_4',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7024, 4, 'EVENT_1580_ret_9'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1580_run_background_event_5',
        "command": 'run_background_event',
        "args": [1569, [_0x40Flags.RETURN_ON_LEVEL_EXIT, _0x40Flags.BIT_6]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1580_set_short_6',
        "command": 'set_short',
        "args": [0x7016, 0x001c],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1580_set_short_7',
        "command": 'set_short',
        "args": [0x7018, 0x0071],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1580_jmp_to_event_8',
        "command": 'jmp_to_event',
        "args": [1573],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1580_ret_9',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
