from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_432_close_dialog_0',
        "command": 'close_dialog'
    },
    {
        "identifier": 'EVENT_432_stop_all_background_events_1',
        "command": 'stop_all_background_events'
    },
    {
        "identifier": 'EVENT_432_stop_background_event_2',
        "command": 'stop_background_event',
        "args": [0x701c]
    },
    {
        "identifier": 'EVENT_432_clear_bit_3',
        "command": 'clear_bit',
        "args": [0x7049, 6]
    },
    {
        "identifier": 'EVENT_432_run_event_as_subroutine_4',
        "command": 'run_event_as_subroutine',
        "args": [65]
    },
    {
        "identifier": 'EVENT_432_enter_area_5',
        "command": 'enter_area',
        "args": [Rooms._124_PIPE_VAULT_AREA_03_LINE_OF_PIPES, RadialDirections.NORTHEAST, 13, 38, 1, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_432_set_bit_6',
        "command": 'set_bit',
        "args": [0x7044, 6]
    },
    {
        "identifier": 'EVENT_432_ret_7',
        "command": 'ret'
    }
]
