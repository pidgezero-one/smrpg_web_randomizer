from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_300_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x705d, 1, 'EVENT_300_run_dialog_12']
    },
    {
        "identifier": 'EVENT_300_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x704c, 6, 'EVENT_300_run_dialog_10']
    },
    {
        "identifier": 'EVENT_300_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x7082, 0, 'EVENT_300_run_dialog_8']
    },
    {
        "identifier": 'EVENT_300_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x7081, 7, 'EVENT_300_run_dialog_6']
    },
    {
        "identifier": 'EVENT_300_run_dialog_4',
        "command": 'run_dialog',
        "args": [537, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_300_ret_5',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_300_run_dialog_6',
        "command": 'run_dialog',
        "args": [725, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_300_ret_7',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_300_run_dialog_8',
        "command": 'run_dialog',
        "args": [726, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_300_ret_9',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_300_run_dialog_10',
        "command": 'run_dialog',
        "args": [2234, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_300_ret_11',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_300_run_dialog_12',
        "command": 'run_dialog',
        "args": [2235, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_300_ret_13',
        "command": 'ret'
    }
]
