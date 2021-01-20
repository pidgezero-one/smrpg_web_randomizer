from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3633_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7084, 3, 'EVENT_3633_jmp_if_bit_set_6'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3633_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x705f, 4, 'EVENT_3633_run_dialog_4'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3633_run_dialog_2',
        "command": 'run_dialog',
        "args": [2415, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3633_ret_3',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3633_run_dialog_4',
        "command": 'run_dialog',
        "args": [3776, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3633_ret_5',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3633_jmp_if_bit_set_6',
        "command": 'jmp_if_bit_set',
        "args": [0x707d, 7, 'EVENT_3633_run_dialog_9'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3633_run_dialog_7',
        "command": 'run_dialog',
        "args": [3777, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3633_ret_8',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3633_run_dialog_9',
        "command": 'run_dialog',
        "args": [3778, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3633_ret_10',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
