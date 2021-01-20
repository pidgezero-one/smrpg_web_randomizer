from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1134_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x706f, 4, 'EVENT_1134_run_dialog_9'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1134_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7054, 7, 'EVENT_1134_run_dialog_7'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1134_run_dialog_2',
        "command": 'run_dialog',
        "args": [2840, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1134_set_bit_3',
        "command": 'set_bit',
        "args": [0x7054, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1134_set_bit_4',
        "command": 'set_bit',
        "args": [0x706f, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1134_set_bit_5',
        "command": 'set_bit',
        "args": [0x7067, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1134_ret_6',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1134_run_dialog_7',
        "command": 'run_dialog',
        "args": [2846, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1134_ret_8',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1134_run_dialog_9',
        "command": 'run_dialog',
        "args": [2831, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1134_ret_10',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]