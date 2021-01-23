from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2063_set_7000_to_7F_mem_var_0',
        "command": 'set_7000_to_7F_mem_var',
        "args": [0xf8c0]
    },
    {
        "identifier": 'EVENT_2063_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7092, 2, 'EVENT_2063_run_dialog_43']
    },
    {
        "identifier": 'EVENT_2063_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x7092, 0, 'EVENT_2063_run_dialog_33']
    },
    {
        "identifier": 'EVENT_2063_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x7092, 1, 'EVENT_2063_run_dialog_19']
    },
    {
        "identifier": 'EVENT_2063_set_bit_4',
        "command": 'set_bit',
        "args": [0x7092, 1]
    },
    {
        "identifier": 'EVENT_2063_run_dialog_5',
        "command": 'run_dialog',
        "args": [2624, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2063_mem_compare_val_6',
        "command": 'mem_compare_val',
        "args": [30]
    },
    {
        "identifier": 'EVENT_2063_jmp_if_comparison_result_is_greater_or_equal_7',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_2063_run_dialog_10']
    },
    {
        "identifier": 'EVENT_2063_run_dialog_8',
        "command": 'run_dialog',
        "args": [2625, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2063_ret_9',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2063_run_dialog_10',
        "command": 'run_dialog',
        "args": [2626, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2063_set_11',
        "command": 'set',
        "args": [0x70a7, 81]
    },
    {
        "identifier": 'EVENT_2063_set_12',
        "command": 'set',
        "args": [0x7000, 524]
    },
    {
        "identifier": 'EVENT_2063_run_event_as_subroutine_13',
        "command": 'run_event_as_subroutine',
        "args": [3829]
    },
    {
        "identifier": 'EVENT_2063_set_bit_14',
        "command": 'set_bit',
        "args": [0x7092, 0]
    },
    {
        "identifier": 'EVENT_2063_set_7000_to_7F_mem_var_15',
        "command": 'set_7000_to_7F_mem_var',
        "args": [0xf8c0]
    },
    {
        "identifier": 'EVENT_2063_mem_compare_val_16',
        "command": 'mem_compare_val',
        "args": [100]
    },
    {
        "identifier": 'EVENT_2063_jmp_if_comparison_result_is_greater_or_equal_17',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_2063_run_dialog_37']
    },
    {
        "identifier": 'EVENT_2063_ret_18',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2063_run_dialog_19',
        "command": 'run_dialog',
        "args": [2627, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2063_mem_compare_val_20',
        "command": 'mem_compare_val',
        "args": [30]
    },
    {
        "identifier": 'EVENT_2063_jmp_if_comparison_result_is_greater_or_equal_21',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_2063_run_dialog_24']
    },
    {
        "identifier": 'EVENT_2063_run_dialog_22',
        "command": 'run_dialog',
        "args": [2628, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2063_ret_23',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2063_run_dialog_24',
        "command": 'run_dialog',
        "args": [2629, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2063_set_25',
        "command": 'set',
        "args": [0x70a7, 81]
    },
    {
        "identifier": 'EVENT_2063_set_26',
        "command": 'set',
        "args": [0x7000, 524]
    },
    {
        "identifier": 'EVENT_2063_run_event_as_subroutine_27',
        "command": 'run_event_as_subroutine',
        "args": [3829]
    },
    {
        "identifier": 'EVENT_2063_set_bit_28',
        "command": 'set_bit',
        "args": [0x7092, 0]
    },
    {
        "identifier": 'EVENT_2063_set_7000_to_7F_mem_var_29',
        "command": 'set_7000_to_7F_mem_var',
        "args": [0xf8c0]
    },
    {
        "identifier": 'EVENT_2063_mem_compare_val_30',
        "command": 'mem_compare_val',
        "args": [100]
    },
    {
        "identifier": 'EVENT_2063_jmp_if_comparison_result_is_greater_or_equal_31',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_2063_run_dialog_37']
    },
    {
        "identifier": 'EVENT_2063_ret_32',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2063_run_dialog_33',
        "command": 'run_dialog',
        "args": [2627, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2063_mem_compare_val_34',
        "command": 'mem_compare_val',
        "args": [100]
    },
    {
        "identifier": 'EVENT_2063_jmp_if_comparison_result_is_greater_or_equal_35',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_2063_run_dialog_37']
    },
    {
        "identifier": 'EVENT_2063_ret_36',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2063_run_dialog_37',
        "command": 'run_dialog',
        "args": [2631, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2063_set_38',
        "command": 'set',
        "args": [0x70a7, 69]
    },
    {
        "identifier": 'EVENT_2063_set_39',
        "command": 'set',
        "args": [0x7000, 524]
    },
    {
        "identifier": 'EVENT_2063_run_event_as_subroutine_40',
        "command": 'run_event_as_subroutine',
        "args": [3829]
    },
    {
        "identifier": 'EVENT_2063_set_bit_41',
        "command": 'set_bit',
        "args": [0x7092, 2]
    },
    {
        "identifier": 'EVENT_2063_ret_42',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2063_run_dialog_43',
        "command": 'run_dialog',
        "args": [2632, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2063_ret_44',
        "command": 'ret'
    }
]
