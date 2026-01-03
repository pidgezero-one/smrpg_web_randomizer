
from randomizer.helpers.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.helpers.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1778_jmp_if_bit_clear_0',
        "command": 'jmp_if_bit_clear',
        "args": [0x7076, 0, 'EVENT_1778_run_event_as_subroutine_3']
    },
    {
        "identifier": 'EVENT_1778_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x707c, 2, 'EVENT_1778_run_event_as_subroutine_3']
    },
    {
        "identifier": 'EVENT_1778_set_short_2',
        "command": "set_var_to_const",
        "args": [0x7022, 0x001e]
    },
    {
        "identifier": 'EVENT_1778_run_event_as_subroutine_3',
        "command": 'run_event_as_subroutine',
        "args": [1844]
    },
    {
        "identifier": 'EVENT_1778_jmp_to_event_13',
        "command": 'run_event_as_subroutine',
        "args": [15]
    },
    {
        "identifier": 'EVENT_1778_jmp_if_bit_clear_7',
        "command": 'jmp_if_bit_clear',
        "args": [0x7087, 0, 'EVENT_1778_ret_26']
    },
    {
        "identifier": 'EVENT_1778_run_event_as_subroutine_25_',
        "command": 'run_event_as_subroutine',
        "args": [3588]
    },
    {
        "identifier": 'EVENT_1778_jmp_if_bit_clear_7_',
        "command": 'jmp_if_bit_clear',
        "args": [0x7099, 7, 'EVENT_1778_ret_26']
    },
    {
        "identifier": 'EVENT_1778_run_event_as_subroutine_25__',
        "command": 'run_event_as_subroutine',
        "args": [3908]
    },
    {
        "identifier": 'EVENT_1778_ret_26',
        "command": 'ret'
    }
]
