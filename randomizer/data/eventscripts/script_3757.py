from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3757_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x707d, 7, 'EVENT_3757_jmp_if_random_above_66_3'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3757_run_dialog_1',
        "command": 'run_dialog',
        "args": [3718, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3757_ret_2',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3757_jmp_if_random_above_66_3',
        "command": 'jmp_if_random_above_66',
        "args": ['EVENT_3757_run_dialog_6'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3757_run_dialog_4',
        "command": 'run_dialog',
        "args": [3867, AreaObjects.MEM_70A8, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3757_jmp_5',
        "command": 'jmp',
        "args": ['EVENT_3757_run_dialog_10'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3757_run_dialog_6',
        "command": 'run_dialog',
        "args": [3868, AreaObjects.MEM_70A8, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3757_jmp_7',
        "command": 'jmp',
        "args": ['EVENT_3757_run_dialog_10'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3757_run_dialog_8',
        "command": 'run_dialog',
        "args": [3869, AreaObjects.MEM_70A8, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3757_jmp_9',
        "command": 'jmp',
        "args": ['EVENT_3757_run_dialog_10'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3757_run_dialog_10',
        "command": 'run_dialog',
        "args": [3870, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3757_ret_11',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
