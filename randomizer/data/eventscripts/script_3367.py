from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3367_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 3, 'EVENT_3366_ret_8'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3367_run_dialog_1',
        "command": 'run_dialog',
        "args": [1925, AreaObjects.MEM_70A8, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3367_run_dialog_2',
        "command": 'run_dialog',
        "args": [1922, AreaObjects.MEM_70A8, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3367_jmp_if_var_equals_byte_3',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70af, 1, 'EVENT_3369_set_short_mem_32'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3367_jmp_if_var_equals_short_4',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7026, 1, 'EVENT_3369_run_dialog_12'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3367_jmp_if_var_equals_short_5',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7026, 2, 'EVENT_3369_run_dialog_10'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3367_jmp_if_var_equals_short_6',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7026, 3, 'EVENT_3369_run_dialog_8'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3367_jmp_if_var_equals_short_7',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7026, 4, 'EVENT_3369_run_dialog_30'],
        "subscript": []
    },
]
