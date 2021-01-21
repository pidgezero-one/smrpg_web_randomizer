from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3759_set_random_0',
        "command": 'set_random',
        "args": [0x7000, 8]
    },
    {
        "identifier": 'EVENT_3759_jmp_if_var_equals_short_1',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 3, 'EVENT_3759_run_dialog_8']
    },
    {
        "identifier": 'EVENT_3759_jmp_if_var_equals_short_2',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 4, 'EVENT_3759_run_dialog_10']
    },
    {
        "identifier": 'EVENT_3759_jmp_if_var_equals_short_3',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 5, 'EVENT_3759_run_dialog_12']
    },
    {
        "identifier": 'EVENT_3759_jmp_if_var_equals_short_4',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 6, 'EVENT_3759_run_dialog_12']
    },
    {
        "identifier": 'EVENT_3759_jmp_if_var_equals_short_5',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 7, 'EVENT_3759_run_dialog_8']
    },
    {
        "identifier": 'EVENT_3759_run_dialog_6',
        "command": 'run_dialog',
        "args": [3595, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_3759_ret_7',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3759_run_dialog_8',
        "command": 'run_dialog',
        "args": [3596, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_3759_ret_9',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3759_run_dialog_10',
        "command": 'run_dialog',
        "args": [3597, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_3759_ret_11',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3759_run_dialog_12',
        "command": 'run_dialog',
        "args": [3598, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_3759_ret_13',
        "command": 'ret'
    }
]
