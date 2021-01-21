from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_708_set_priority_0',
        "command": 'set_priority',
        "args": [2]
    },
    {
        "identifier": 'ACTION_708_face_southwest_1',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_708_fixed_f_coord_on_2',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_708_set_animation_speed_3',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FASTER, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_708_transfer_to_xyzf_4',
        "command": 'transfer_to_xyzf',
        "args": [1, 50, 0, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_708_object_memory_clear_bit_5',
        "command": 'object_memory_clear_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_708_set_solidity_bits_6',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_708_set_random_7',
        "command": 'set_random',
        "args": [0x700c, 30]
    },
    {
        "identifier": 'ACTION_708_add_short_8',
        "command": 'add_short',
        "args": [0x700c, 0x01]
    },
    {
        "identifier": 'ACTION_708_load_mem_9',
        "command": 'load_mem',
        "args": [0x700c]
    },
    {
        "identifier": 'ACTION_708_pause_10',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_708_end_loop_11',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_708_jmp_if_bit_set_12',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 4, 'ACTION_708_shift_southwest_pixels_14']
    },
    {
        "identifier": 'ACTION_708_play_sound_13',
        "command": 'play_sound',
        "args": [Sounds._049_BIG_SHELL_HIT, 4]
    },
    {
        "identifier": 'ACTION_708_shift_southwest_pixels_14',
        "command": 'shift_southwest_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_708_db_15',
        "command": 'db',
        "args": [0x3a, 0x17, 0x00, 0x03, 0xbc, 0x82]
    },
    {
        "identifier": 'ACTION_708_jump_to_height_16',
        "command": 'jump_to_height',
        "args": [24]
    },
    {
        "identifier": 'ACTION_708_walk_1_step_southeast_17',
        "command": 'walk_1_step_southeast'
    },
    {
        "identifier": 'ACTION_708_jmp_18',
        "command": 'jmp',
        "args": ['ACTION_708_db_15']
    },
    {
        "identifier": 'ACTION_708_set_bit_19',
        "command": 'set_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'ACTION_708_jump_to_height_20',
        "command": 'jump_to_height',
        "args": [24]
    },
    {
        "identifier": 'ACTION_708_walk_1_step_southeast_21',
        "command": 'walk_1_step_southeast'
    },
    {
        "identifier": 'ACTION_708_set_700C_to_object_coord_22',
        "command": 'set_700C_to_object_coord',
        "args": [AreaObjects.DUMMY_0X07, Coords.X, CoordUnits.PIXEL]
    },
    {
        "identifier": 'ACTION_708_mem_compare_23',
        "command": 'mem_compare',
        "args": [0x700c, 5888]
    },
    {
        "identifier": 'ACTION_708_jmp_if_comparison_result_is_lesser_24',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['ACTION_708_jump_to_height_20']
    },
    {
        "identifier": 'ACTION_708_ret_25',
        "command": 'ret'
    }
]
