from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_20_visibility_off_0',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_20_clear_solidity_bits_1',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_20_set_solidity_bits_2',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_JUMP_THROUGH]]
    },
    {
        "identifier": 'ACTION_20_db_3',
        "command": 'db',
        "args": [0xc8, 0x80]
    },
    {
        "identifier": 'ACTION_20_set_short_4',
        "command": 'set_short',
        "args": [0x701a, 0x0005]
    },
    {
        "identifier": 'ACTION_20_db_5',
        "command": 'db',
        "args": [0x9a]
    },
    {
        "identifier": 'ACTION_20_set_700C_to_object_coord_6',
        "command": 'set_700C_to_object_coord',
        "args": [AreaObjects.MARIO, Coords.F, []]
    },
    {
        "identifier": 'ACTION_20_jmp_if_700C_equals_short_7',
        "command": 'jmp_if_700C_equals_short',
        "args": [1, 'ACTION_20_transfer_xyzf_pixels_14']
    },
    {
        "identifier": 'ACTION_20_jmp_if_700C_equals_short_8',
        "command": 'jmp_if_700C_equals_short',
        "args": [3, 'ACTION_20_transfer_xyzf_pixels_16']
    },
    {
        "identifier": 'ACTION_20_jmp_if_700C_equals_short_9',
        "command": 'jmp_if_700C_equals_short',
        "args": [5, 'ACTION_20_transfer_xyzf_pixels_18']
    },
    {
        "identifier": 'ACTION_20_jmp_if_700C_equals_short_10',
        "command": 'jmp_if_700C_equals_short',
        "args": [7, 'ACTION_20_transfer_xyzf_pixels_20']
    },
    {
        "identifier": 'ACTION_20_jmp_if_random_above_66_11',
        "command": 'jmp_if_random_above_66',
        "args": [0x0a0e, 'ACTION_20_transfer_xyzf_pixels_20']
    },
    {
        "identifier": 'ACTION_20_jmp_if_random_above_128_12',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_20_transfer_xyzf_pixels_16']
    },
    {
        "identifier": 'ACTION_20_jmp_13',
        "command": 'jmp',
        "args": ['ACTION_20_transfer_xyzf_pixels_14']
    },
    {
        "identifier": 'ACTION_20_transfer_xyzf_pixels_14',
        "command": 'transfer_xyzf_pixels',
        "args": [32, 16, 0, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_20_jmp_15',
        "command": 'jmp',
        "args": ['ACTION_20_db_21']
    },
    {
        "identifier": 'ACTION_20_transfer_xyzf_pixels_16',
        "command": 'transfer_xyzf_pixels',
        "args": [224, 16, 0, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_20_jmp_17',
        "command": 'jmp',
        "args": ['ACTION_20_db_21']
    },
    {
        "identifier": 'ACTION_20_transfer_xyzf_pixels_18',
        "command": 'transfer_xyzf_pixels',
        "args": [224, 240, 0, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_20_jmp_19',
        "command": 'jmp',
        "args": ['ACTION_20_db_21']
    },
    {
        "identifier": 'ACTION_20_transfer_xyzf_pixels_20',
        "command": 'transfer_xyzf_pixels',
        "args": [32, 240, 0, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_20_db_21',
        "command": 'db',
        "args": [0xc7, 0x07]
    },
    {
        "identifier": 'ACTION_20_db_22',
        "command": 'db',
        "args": [0xc8, 0x87]
    },
    {
        "identifier": 'ACTION_20_db_23',
        "command": 'db',
        "args": [0xfd, 0xca]
    },
    {
        "identifier": 'ACTION_20_jmp_if_700C_equals_short_24',
        "command": 'jmp_if_700C_equals_short',
        "args": [255, 'ACTION_18_ret_61']
    },
    {
        "identifier": 'ACTION_20_mem_compare_25',
        "command": 'mem_compare',
        "args": [0x7010, 12544]
    },
    {
        "identifier": 'ACTION_20_jmp_if_comparison_result_is_greater_or_equal_26',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['ACTION_20_ret_61']
    },
    {
        "identifier": 'ACTION_20_mem_compare_27',
        "command": 'mem_compare',
        "args": [0x7010, 3584]
    },
    {
        "identifier": 'ACTION_20_jmp_if_comparison_result_is_lesser_28',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['ACTION_20_ret_61']
    },
    {
        "identifier": 'ACTION_20_mem_compare_29',
        "command": 'mem_compare',
        "args": [0x7012, 13056]
    },
    {
        "identifier": 'ACTION_20_jmp_if_comparison_result_is_greater_or_equal_30',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['ACTION_20_ret_61']
    },
    {
        "identifier": 'ACTION_20_mem_compare_31',
        "command": 'mem_compare',
        "args": [0x7012, 8192]
    },
    {
        "identifier": 'ACTION_20_jmp_if_comparison_result_is_lesser_32',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['ACTION_20_ret_61']
    },
    {
        "identifier": 'ACTION_20_visibility_on_33',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_20_floating_on_34',
        "command": 'floating_on'
    },
    {
        "identifier": 'ACTION_20_pause_35',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_20_db_36',
        "command": 'db',
        "args": [0xfd, 0x3d, 0x07, 0x43, 0x0a]
    },
    {
        "identifier": 'ACTION_20_pause_37',
        "command": 'pause',
        "args": [120]
    },
    {
        "identifier": 'ACTION_20_start_loop_n_times_38',
        "command": 'start_loop_n_times',
        "args": [1]
    },
    {
        "identifier": 'ACTION_20_visibility_off_39',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_20_pause_40',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_20_visibility_on_41',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_20_pause_42',
        "command": 'pause',
        "args": [6]
    },
    {
        "identifier": 'ACTION_20_end_loop_43',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_20_start_loop_n_times_44',
        "command": 'start_loop_n_times',
        "args": [3]
    },
    {
        "identifier": 'ACTION_20_visibility_off_45',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_20_pause_46',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'ACTION_20_visibility_on_47',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_20_pause_48',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'ACTION_20_end_loop_49',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_20_clear_solidity_bits_50',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_20_start_loop_n_times_51',
        "command": 'start_loop_n_times',
        "args": [7]
    },
    {
        "identifier": 'ACTION_20_visibility_off_52',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_20_pause_53',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_20_visibility_on_54',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_20_pause_55',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_20_end_loop_56',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_20_clear_bit_57',
        "command": 'clear_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'ACTION_20_transfer_to_xyzf_58',
        "command": 'transfer_to_xyzf',
        "args": [21, 117, 0, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_20_object_memory_clear_bit_59',
        "command": 'object_memory_clear_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_20_visibility_off_60',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_20_ret_61',
        "command": 'ret'
    }
]
