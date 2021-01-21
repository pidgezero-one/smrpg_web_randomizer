from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_739_run_dialog_0',
        "command": 'run_dialog',
        "args": [2533, AreaObjects.NPC_12, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_739_run_dialog_1',
        "command": 'run_dialog',
        "args": [2534, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_739_jmp_if_dialog_option_b_2',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_739_run_dialog_6']
    },
    {
        "identifier": 'EVENT_739_run_dialog_3',
        "command": 'run_dialog',
        "args": [2535, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_739_run_dialog_4',
        "command": 'run_dialog',
        "args": [2536, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_739_ret_5',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_739_run_dialog_6',
        "command": 'run_dialog',
        "args": [2537, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_739_ret_7',
        "command": 'ret'
    }
]
