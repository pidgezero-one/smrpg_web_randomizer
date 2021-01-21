from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3720_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x705f, 7, 'EVENT_3720_run_dialog_10']
    },
    {
        "identifier": 'EVENT_3720_set_bit_1',
        "command": 'set_bit',
        "args": [0x705f, 7]
    },
    {
        "identifier": 'EVENT_3720_stop_sound_2',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3720_stop_sound_3',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3720_stop_sound_4',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3720_stop_sound_5',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3720_set_6',
        "command": 'set',
        "args": [0x70a7, 116]
    },
    {
        "identifier": 'EVENT_3720_set_7',
        "command": 'set',
        "args": [0x7000, 524]
    },
    {
        "identifier": 'EVENT_3720_run_event_as_subroutine_8',
        "command": 'run_event_as_subroutine',
        "args": [3828]
    },
    {
        "identifier": 'EVENT_3720_ret_9',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3720_run_dialog_10',
        "command": 'run_dialog',
        "args": [3667, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_3720_ret_11',
        "command": 'ret'
    }
]
