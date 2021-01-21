from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2530_play_sound_0',
        "command": 'play_sound',
        "args": [Sounds._110_ABSTRACT_MUSIC, 6]
    },
    {
        "identifier": 'EVENT_2530_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x709a, 0, 'EVENT_2530_run_dialog_5']
    },
    {
        "identifier": 'EVENT_2530_run_dialog_2',
        "command": 'run_dialog',
        "args": [3106, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2530_play_sound_3',
        "command": 'play_sound',
        "args": [Sounds._000_SILENCE, 6]
    },
    {
        "identifier": 'EVENT_2530_ret_4',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2530_run_dialog_5',
        "command": 'run_dialog',
        "args": [3275, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2530_play_sound_6',
        "command": 'play_sound',
        "args": [Sounds._000_SILENCE, 6]
    },
    {
        "identifier": 'EVENT_2530_ret_7',
        "command": 'ret'
    }
]
