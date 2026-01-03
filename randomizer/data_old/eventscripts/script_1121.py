
from randomizer.helpers.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.helpers.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": "EVENT_1121_sequence_setter_2",
        "command": "run_event_as_subroutine",
        "args": [807]
    },
    {
        "identifier": 'EVENT_1121_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 7, 'EVENT_1121_run_event_as_subroutine_3']
    },
    {
        "identifier": 'EVENT_1121_fade_in_from_black_async_1',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_1121_ret_2',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1121_run_event_as_subroutine_3',
        "command": 'run_event_as_subroutine',
        "args": [81]
    },
    {
        "identifier": 'EVENT_1121_run_event_as_subroutine_25___',
        "command": 'run_event_as_subroutine',
        "args": [3588]
    },
    {
        "identifier": 'EVENT_1121_jmp_if_bit_clear_7___',
        "command": 'jmp_if_bit_clear',
        "args": [0x7099, 7, 'EVENT_1121_ret_4']
    },
    {
        "identifier": 'EVENT_1121_run_event_as_subroutine_25____',
        "command": 'run_event_as_subroutine',
        "args": [3904]
    },
    {
        "identifier": 'EVENT_1121_ret_4',
        "command": 'ret'
    }
]
