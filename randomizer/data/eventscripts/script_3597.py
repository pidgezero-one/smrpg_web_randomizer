from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3597_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x708b, 5, 'EVENT_3596_jmp_if_bit_set_0']
    },
    {
        "identifier": 'EVENT_3597_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 5, 'EVENT_3597_run_event_as_subroutine_7']
    },
    {
        "identifier": 'EVENT_3597_run_dialog_2',
        "command": 'run_dialog',
        "args": [2339, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_3597_jmp_if_dialog_option_b_3',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_3584_ret_0']
    },
    {
        "identifier": 'EVENT_3597_run_dialog_4',
        "command": 'run_dialog',
        "args": [2340, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_3597_clear_bit_5',
        "command": 'clear_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_3597_ret_6',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3597_run_event_as_subroutine_7',
        "command": 'run_event_as_subroutine',
        "args": [456]
    },
    {
        "identifier": 'EVENT_3597_run_dialog_8',
        "command": 'run_dialog',
        "args": [2336, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_3597_clear_bit_9',
        "command": 'clear_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_3597_run_background_event_10',
        "command": 'run_background_event',
        "args": [469, [_0x40Flags.RETURN_ON_LEVEL_EXIT, _0x40Flags.BIT_7]]
    },
    {
        "identifier": 'EVENT_3597_ret_11',
        "command": 'ret'
    }
]
