from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1814_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 7, 'EVENT_1814_ret_10'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1814_jmp_if_bit_clear_1',
        "command": 'jmp_if_bit_clear',
        "args": [0x708a, 0, 'EVENT_1814_ret_10'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1814_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'EVENT_1814_ret_10'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1814_set_bit_3',
        "command": 'set_bit',
        "args": [0x7043, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1814_clear_bit_4',
        "command": 'clear_bit',
        "args": [0x7044, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1814_fade_out_music_to_volume_5',
        "command": 'fade_out_music_to_volume',
        "args": [2, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1814_play_sound_6',
        "command": 'play_sound',
        "args": [Sounds._147_CLICK, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1814_set_short_7',
        "command": 'set_short',
        "args": [0x7024, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1814_set_short_8',
        "command": 'set_short',
        "args": [0x7026, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1814_run_background_event_9',
        "command": 'run_background_event',
        "args": [1815, [_0x40Flags.RETURN_ON_LEVEL_EXIT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1814_ret_10',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
