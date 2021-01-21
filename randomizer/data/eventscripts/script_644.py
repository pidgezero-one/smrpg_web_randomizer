from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_644_jmp_0',
        "command": 'jmp',
        "args": ['EVENT_256_ret_0']
    },
    {
        "identifier": 'EVENT_644_stop_sound_1',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_644_stop_sound_2',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_644_enable_controls_until_return_3',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]]
    },
    {
        "identifier": 'EVENT_644_clear_bit_4',
        "command": 'clear_bit',
        "args": [0x7043, 3]
    },
    {
        "identifier": 'EVENT_644_jmp_if_bit_clear_5',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 1, 'EVENT_256_ret_0']
    },
    {
        "identifier": 'EVENT_644_set_short_6',
        "command": 'set_short',
        "args": [0x701c, 0x0014]
    },
    {
        "identifier": 'EVENT_644_run_background_event_with_pause_return_on_exit_7',
        "command": 'run_background_event_with_pause_return_on_exit',
        "args": [3809, 0x701c, [13]]
    },
    {
        "identifier": 'EVENT_644_ret_8',
        "command": 'ret'
    }
]
