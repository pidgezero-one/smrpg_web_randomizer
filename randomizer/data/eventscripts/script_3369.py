from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3369_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 4, 'EVENT_3366_ret_8'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3369_run_dialog_1',
        "command": 'run_dialog',
        "args": [1925, AreaObjects.MEM_70A8, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3369_run_dialog_2',
        "command": 'run_dialog',
        "args": [1924, AreaObjects.MEM_70A8, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3369_jmp_if_var_equals_byte_3',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70af, 1, 'EVENT_3369_set_short_mem_32'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3369_jmp_if_var_equals_short_4',
        "command": 'jmp_if_var_equals_short',
        "args": [0x702a, 1, 'EVENT_3369_run_dialog_12'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3369_jmp_if_var_equals_short_5',
        "command": 'jmp_if_var_equals_short',
        "args": [0x702a, 2, 'EVENT_3369_run_dialog_10'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3369_jmp_if_var_equals_short_6',
        "command": 'jmp_if_var_equals_short',
        "args": [0x702a, 3, 'EVENT_3369_run_dialog_8'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3369_jmp_if_var_equals_short_7',
        "command": 'jmp_if_var_equals_short',
        "args": [0x702a, 4, 'EVENT_3369_run_dialog_30'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3369_run_dialog_8',
        "command": 'run_dialog',
        "args": [1926, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3369_ret_9',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3369_run_dialog_10',
        "command": 'run_dialog',
        "args": [1927, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3369_ret_11',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3369_run_dialog_12',
        "command": 'run_dialog',
        "args": [1928, AreaObjects.MEM_70A8, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3369_jmp_to_subroutine_13',
        "command": 'jmp_to_subroutine',
        "args": [0x5997],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3369_run_dialog_14',
        "command": 'run_dialog',
        "args": [1929, AreaObjects.MEM_70A8, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3369_jmp_to_subroutine_15',
        "command": 'jmp_to_subroutine',
        "args": [0x5997],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3369_run_dialog_16',
        "command": 'run_dialog',
        "args": [1930, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3369_ret_17',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3369_jmp_if_var_equals_short_18',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7024, 2, 'EVENT_3369_run_dialog_22'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3369_jmp_if_var_equals_short_19',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7026, 2, 'EVENT_3369_run_dialog_24'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3369_jmp_if_var_equals_short_20',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7028, 2, 'EVENT_3369_run_dialog_26'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3369_jmp_if_var_equals_short_21',
        "command": 'jmp_if_var_equals_short',
        "args": [0x702a, 2, 'EVENT_3369_run_dialog_28'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3369_run_dialog_22',
        "command": 'run_dialog',
        "args": [1921, AreaObjects.MEM_70A8, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3369_ret_23',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3369_run_dialog_24',
        "command": 'run_dialog',
        "args": [1922, AreaObjects.MEM_70A8, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3369_ret_25',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3369_run_dialog_26',
        "command": 'run_dialog',
        "args": [1923, AreaObjects.MEM_70A8, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3369_ret_27',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3369_run_dialog_28',
        "command": 'run_dialog',
        "args": [1924, AreaObjects.MEM_70A8, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3369_ret_29',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3369_run_dialog_30',
        "command": 'run_dialog',
        "args": [1931, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3369_ret_31',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3369_set_short_mem_32',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70ae],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3369_add_33',
        "command": 'add',
        "args": [0x7000, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3369_run_dialog_34',
        "command": 'run_dialog',
        "args": [1934, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3369_jmp_if_dialog_option_b_35',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_3366_ret_8'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3369_add_36',
        "command": 'add',
        "args": [0x70ae, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3369_set_short_mem_37',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70a8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3369_add_38',
        "command": 'add',
        "args": [0x7000, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3369_set_mem_704x_at_7000_bit_39',
        "command": 'set_mem_704x_at_7000_bit',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3369_set_short_mem_40',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70ae],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3369_jmp_if_var_equals_byte_41',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70a8, 21, 'EVENT_3369_set_short_mem_45'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3369_jmp_if_var_equals_byte_42',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70a8, 23, 'EVENT_3369_set_short_mem_47'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3369_jmp_if_var_equals_byte_43',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70a8, 22, 'EVENT_3369_set_short_mem_49'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3369_jmp_if_var_equals_byte_44',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70a8, 24, 'EVENT_3369_set_short_mem_51'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3369_set_short_mem_45',
        "command": 'set_short_mem',
        "args": [0x702c, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3369_ret_46',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3369_set_short_mem_47',
        "command": 'set_short_mem',
        "args": [0x702e, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3369_ret_48',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3369_set_short_mem_49',
        "command": 'set_short_mem',
        "args": [0x7030, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3369_ret_50',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3369_set_short_mem_51',
        "command": 'set_short_mem',
        "args": [0x7032, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3369_ret_52',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
