from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_311_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x704c, 6, 'EVENT_311_run_dialog_13'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_311_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 3, 'EVENT_256_ret_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_311_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x7081, 5, 'EVENT_311_run_dialog_7'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_311_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x7082, 2, 'EVENT_311_run_dialog_11'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_311_jmp_if_bit_set_4',
        "command": 'jmp_if_bit_set',
        "args": [0x7081, 6, 'EVENT_311_set_bit_9'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_311_run_dialog_5',
        "command": 'run_dialog',
        "args": [590, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_311_ret_6',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_311_run_dialog_7',
        "command": 'run_dialog',
        "args": [591, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_311_ret_8',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_311_set_bit_9',
        "command": 'set_bit',
        "args": [0x7043, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_311_jmp_to_event_10',
        "command": 'jmp_to_event',
        "args": [332],
        "subscript": []
    },
    {
        "identifier": 'EVENT_311_run_dialog_11',
        "command": 'run_dialog',
        "args": [604, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_311_ret_12',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_311_run_dialog_13',
        "command": 'run_dialog',
        "args": [2224, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_311_ret_14',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
