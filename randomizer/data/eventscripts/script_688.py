from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_688_set_7000_to_current_level_0',
        "command": 'set_7000_to_current_level'
    },
    {
        "identifier": 'EVENT_688_jmp_if_7000_equals_short_1',
        "command": 'jmp_if_7000_equals_short',
        "args": [65, 'EVENT_688_jmp_if_bit_clear_4']
    },
    {
        "identifier": 'EVENT_688_run_dialog_2',
        "command": 'run_dialog',
        "args": [2112, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_688_ret_3',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_688_jmp_if_bit_clear_4',
        "command": 'jmp_if_bit_clear',
        "args": [0x708b, 5, 'EVENT_688_run_dialog_7']
    },
    {
        "identifier": 'EVENT_688_run_dialog_5',
        "command": 'run_dialog',
        "args": [2177, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_688_ret_6',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_688_run_dialog_7',
        "command": 'run_dialog',
        "args": [2183, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_688_ret_8',
        "command": 'ret'
    }
]
