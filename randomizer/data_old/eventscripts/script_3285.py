
from randomizer.helpers.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.helpers.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3285_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7055, 6, 'EVENT_3285_jmp_if_bit_clear_3']
    },
    {
        "identifier": 'EVENT_3285_set_bit_1',
        "command": 'set_bit',
        "args": [0x7055, 6]
    },
    {
        "identifier": 'EVENT_3285_apply_tile_mod_2',
        "command": 'apply_tile_mod',
        "args": [Rooms._131_SEA_AREA_04_BUNCH_OF_ZEOSTARS, 32, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_3285_jmp_if_bit_clear_3',
        "command": 'jmp_if_bit_clear',
        "args": [0x7076, 0, 'EVENT_3285_jmp_to_event_9']
    },
    {
        "identifier": 'EVENT_3285_set_7000_to_current_level_4',
        "command": 'set_7000_to_current_level'
    },
    {
        "identifier": 'EVENT_3285_jmp_if_7000_equals_short_5',
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 133, 'EVENT_3285_set_short_8']
    },
    {
        "identifier": 'EVENT_3285_set_short_6',
        "command": "set_var_to_const",
        "args": [0x7022, 0x0005]
    },
    {
        "identifier": 'EVENT_3285_jmp_7',
        "command": 'jmp',
        "args": ['EVENT_3285_jmp_to_event_9']
    },
    {
        "identifier": 'EVENT_3285_set_short_8',
        "command": "set_var_to_const",
        "args": [0x7022, 0x0028]
    },
    {
        "identifier": 'EVENT_3285_jmp_if_bit_clear_7',
        "command": 'jmp_if_bit_clear',
        "args": [0x7087, 0, 'EVENT_3285_jmp_to_event_9']
    },
    {
        "identifier": 'EVENT_3285_run_event_as_subroutine_25_',
        "command": 'run_event_as_subroutine',
        "args": [3588]
    },
    {
        "identifier": 'EVENT_3285_jmp_if_bit_clear_7_',
        "command": 'jmp_if_bit_clear',
        "args": [0x7099, 7, 'EVENT_3285_jmp_to_event_9']
    },
    {
        "identifier": 'EVENT_3285_run_event_as_subroutine_25__',
        "command": 'run_event_as_subroutine',
        "args": [3905]
    },
    {
        "identifier": 'EVENT_3285_jmp_to_event_9',
        "command": 'jmp_to_event',
        "args": [15]
    }
]
