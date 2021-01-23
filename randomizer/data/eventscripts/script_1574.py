from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1574_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'EVENT_1574_ret_11']
    },
    {
        "identifier": 'EVENT_1574_clear_bit_1',
        "command": 'clear_bit',
        "args": [0x7044, 3]
    },
    {
        "identifier": 'EVENT_1574_set_bit_2',
        "command": 'set_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_1574_inc_short_3',
        "command": 'inc_short',
        "args": [0x7024]
    },
    {
        "identifier": 'EVENT_1574_jmp_if_var_equals_short_4',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7024, 1, 'EVENT_1574_jmp_if_var_not_equals_short_6']
    },
    {
        "identifier": 'EVENT_1574_run_background_event_5',
        "command": 'run_background_event',
        "args": [1586, [_0x40Flags.RETURN_ON_LEVEL_EXIT, _0x40Flags.BIT_6]]
    },
    {
        "identifier": 'EVENT_1574_jmp_if_var_not_equals_short_6',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7024, 2, 'EVENT_1574_set_short_8']
    },
    {
        "identifier": 'EVENT_1574_adjust_music_tempo_7',
        "command": 'adjust_music_tempo',
        "args": [MusicDirections.SPEED_UP, 24, 255]
    },
    {
        "identifier": 'EVENT_1574_set_short_8',
        "command": 'set_short',
        "args": [0x7016, 0x0006]
    },
    {
        "identifier": 'EVENT_1574_set_short_9',
        "command": 'set_short',
        "args": [0x7018, 0x001d]
    },
    {
        "identifier": 'EVENT_1574_jmp_to_event_10',
        "command": 'jmp_to_event',
        "args": [1573]
    },
    {
        "identifier": 'EVENT_1574_ret_11',
        "command": 'ret'
    }
]
