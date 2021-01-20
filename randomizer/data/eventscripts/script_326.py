from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_326_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x705d, 1, 'EVENT_326_jmp_if_random_above_128_9'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_326_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7081, 3, 'EVENT_326_jmp_if_random_above_128_4'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_326_run_dialog_2',
        "command": 'run_dialog',
        "args": [696, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_326_ret_3',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_326_jmp_if_random_above_128_4',
        "command": 'jmp_if_random_above_128',
        "args": ['EVENT_326_run_dialog_7'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_326_run_dialog_5',
        "command": 'run_dialog',
        "args": [564, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_326_ret_6',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_326_run_dialog_7',
        "command": 'run_dialog',
        "args": [565, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_326_ret_8',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_326_jmp_if_random_above_128_9',
        "command": 'jmp_if_random_above_128',
        "args": ['EVENT_326_run_dialog_12'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_326_run_dialog_10',
        "command": 'run_dialog',
        "args": [2299, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_326_ret_11',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_326_run_dialog_12',
        "command": 'run_dialog',
        "args": [2300, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_326_ret_13',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
