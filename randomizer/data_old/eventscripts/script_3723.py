
from randomizer.helpers.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.helpers.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3723_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x705f, 6, 'EVENT_3723_run_dialog_85']
    },
    {
        "identifier": 'EVENT_3723_set_4',
        "command": "set_var_to_const",
        "args": [0x70ae, 16]
    },
    {
        "identifier": 'EVENT_3723_run_event_as_subroutine_8',
        "command": 'run_event_as_subroutine',
        "args": [179]
    },
    {
        "identifier": 'EVENT_3723_set_bit_29',
        "command": 'set_bit',
        "args": [0x705f, 6]
    },
    {
        "identifier": 'EVENT_3723_clear_bit_30',
        "command": 'clear_bit',
        "args": [0x704c, 0]
    },
    {
        "identifier": 'EVENT_3723_clear_bit_31',
        "command": 'clear_bit',
        "args": [0x704c, 1]
    },
    {
        "identifier": 'EVENT_3723_ret_32',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3723_run_dialog_85',
        "command": 'run_dialog',
        "args": [3648, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_3723_ret_88',
        "command": 'ret'
    }
]
