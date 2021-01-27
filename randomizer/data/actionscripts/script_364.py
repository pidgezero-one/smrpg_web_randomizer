from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_364_set_priority_0',
        "command": 'set_priority',
        "args": [2]
    },
    {
        "identifier": 'ACTION_364_fixed_f_coord_on_1',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_364_set_animation_speed_2',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_364_jmp_if_random_above_128_3',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_364_transfer_to_xyzf_6']
    },
    {
        "identifier": 'ACTION_364_transfer_to_xyzf_4',
        "command": 'transfer_to_xyzf',
        "args": [1, 50, 0, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_364_jmp_5',
        "command": 'jmp',
        "args": ['ACTION_364_visibility_on_9']
    },
    {
        "identifier": 'ACTION_364_transfer_to_xyzf_6',
        "command": 'transfer_to_xyzf',
        "args": [2, 48, 0, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_364_jmp_7',
        "command": 'jmp',
        "args": ['ACTION_364_visibility_on_9']
    },
    {
        "identifier": 'ACTION_364_transfer_to_xyzf_8',
        "command": 'transfer_to_xyzf',
        "args": [3, 46, 0, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_364_visibility_on_9',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_364_object_memory_clear_bit_10',
        "command": 'object_memory_clear_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_364_set_solidity_bits_11',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_364_walk_1_step_southeast_12',
        "command": 'walk_1_step_southeast'
    },
    {
        "identifier": 'ACTION_364_set_700C_to_object_coord_13',
        "command": 'set_700C_to_object_coord',
        "args": [AreaObjects.DUMMY_0X07, Coords.X, [], CoordUnits.PIXEL]
    },
    {
        "identifier": 'ACTION_364_mem_compare_val_14',
        "command": 'mem_compare_val',
        "args": [5888]
    },
    {
        "identifier": 'ACTION_364_jmp_if_comparison_result_is_lesser_15',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['ACTION_364_walk_1_step_southeast_12']
    },
    {
        "identifier": 'ACTION_364_ret_16',
        "command": 'ret'
    }
]
