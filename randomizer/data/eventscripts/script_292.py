from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_292_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x704c, 6, 'EVENT_292_run_dialog_13'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_292_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7081, 5, 'EVENT_292_jmp_if_bit_set_5'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_292_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x7081, 3, 'EVENT_292_jmp_if_bit_set_5'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_292_run_dialog_3',
        "command": 'run_dialog',
        "args": [530, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_292_ret_4',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_292_jmp_if_bit_set_5',
        "command": 'jmp_if_bit_set',
        "args": [0x7081, 7, 'EVENT_292_jmp_if_bit_set_8'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_292_run_dialog_6',
        "command": 'run_dialog',
        "args": [605, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_292_ret_7',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_292_jmp_if_bit_set_8',
        "command": 'jmp_if_bit_set',
        "args": [0x7082, 0, 'EVENT_292_run_dialog_11'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_292_run_dialog_9',
        "command": 'run_dialog',
        "args": [724, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_292_ret_10',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_292_run_dialog_11',
        "command": 'run_dialog',
        "args": [605, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_292_ret_12',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_292_run_dialog_13',
        "command": 'run_dialog',
        "args": [2232, AreaObjects.MEM_70A8, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_292_pause_14',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_292_play_sound_15',
        "command": 'play_sound',
        "args": [Sounds._026_LAUGHING_BOWSER, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_292_pause_16',
        "command": 'pause',
        "args": [40],
        "subscript": []
    },
    {
        "identifier": 'EVENT_292_run_dialog_17',
        "command": 'run_dialog',
        "args": [2233, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_292_ret_18',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
