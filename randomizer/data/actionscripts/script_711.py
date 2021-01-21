from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_711_fixed_f_coord_on_0',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_711_dec_1',
        "command": 'dec',
        "args": [0x70ae]
    },
    {
        "identifier": 'ACTION_711_play_sound_2',
        "command": 'play_sound',
        "args": [Sounds._033_JUMPING_BOUNCING_FISH, 4]
    },
    {
        "identifier": 'ACTION_711_set_animation_speed_3',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_711_set_700C_to_pressed_button_4',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_711_jmp_if_var_equals_short_5',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 23, 'ACTION_711_db_25']
    },
    {
        "identifier": 'ACTION_711_jmp_if_var_equals_short_6',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 24, 'ACTION_711_db_16']
    },
    {
        "identifier": 'ACTION_711_db_7',
        "command": 'db',
        "args": [0x20, 0x00]
    },
    {
        "identifier": 'ACTION_711_walk_1_step_southeast_8',
        "command": 'walk_1_step_southeast'
    },
    {
        "identifier": 'ACTION_711_set_700C_to_object_coord_9',
        "command": 'set_700C_to_object_coord',
        "args": [AreaObjects.DUMMY_0X07, Coords.X, CoordUnits.PIXEL]
    },
    {
        "identifier": 'ACTION_711_mem_compare_10',
        "command": 'mem_compare',
        "args": [0x700c, 5888]
    },
    {
        "identifier": 'ACTION_711_jmp_if_comparison_result_is_lesser_11',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['ACTION_711_walk_1_step_southeast_8']
    },
    {
        "identifier": 'ACTION_711_transfer_to_xyzf_12',
        "command": 'transfer_to_xyzf',
        "args": [13, 67, 0, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_711_jmp_if_bit_clear_13',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 3, 'ACTION_711_jmp_15']
    },
    {
        "identifier": 'ACTION_711_jump_to_subroutine_14',
        "command": 'jump_to_subroutine',
        "args": [0x8391]
    },
    {
        "identifier": 'ACTION_711_jmp_15',
        "command": 'jmp',
        "args": ['ACTION_707_set_priority_0']
    },
    {
        "identifier": 'ACTION_711_db_16',
        "command": 'db',
        "args": [0x20, 0x00]
    },
    {
        "identifier": 'ACTION_711_walk_1_step_southeast_17',
        "command": 'walk_1_step_southeast'
    },
    {
        "identifier": 'ACTION_711_set_700C_to_object_coord_18',
        "command": 'set_700C_to_object_coord',
        "args": [AreaObjects.DUMMY_0X07, Coords.X, CoordUnits.PIXEL]
    },
    {
        "identifier": 'ACTION_711_mem_compare_19',
        "command": 'mem_compare',
        "args": [0x700c, 5888]
    },
    {
        "identifier": 'ACTION_711_jmp_if_comparison_result_is_lesser_20',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['ACTION_711_walk_1_step_southeast_17']
    },
    {
        "identifier": 'ACTION_711_transfer_to_xyzf_21',
        "command": 'transfer_to_xyzf',
        "args": [12, 69, 0, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_711_jmp_if_bit_clear_22',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 3, 'ACTION_711_jmp_24']
    },
    {
        "identifier": 'ACTION_711_jump_to_subroutine_23',
        "command": 'jump_to_subroutine',
        "args": [0x8391]
    },
    {
        "identifier": 'ACTION_711_jmp_24',
        "command": 'jmp',
        "args": ['ACTION_707_set_priority_0']
    },
    {
        "identifier": 'ACTION_711_db_25',
        "command": 'db',
        "args": [0x20, 0x00]
    },
    {
        "identifier": 'ACTION_711_walk_1_step_southeast_26',
        "command": 'walk_1_step_southeast'
    },
    {
        "identifier": 'ACTION_711_set_700C_to_object_coord_27',
        "command": 'set_700C_to_object_coord',
        "args": [AreaObjects.DUMMY_0X07, Coords.X, CoordUnits.PIXEL]
    },
    {
        "identifier": 'ACTION_711_mem_compare_28',
        "command": 'mem_compare',
        "args": [0x700c, 5888]
    },
    {
        "identifier": 'ACTION_711_jmp_if_comparison_result_is_lesser_29',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['ACTION_711_walk_1_step_southeast_26']
    },
    {
        "identifier": 'ACTION_711_transfer_to_xyzf_30',
        "command": 'transfer_to_xyzf',
        "args": [11, 71, 0, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_711_jmp_if_bit_clear_31',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 3, 'ACTION_711_jmp_34']
    },
    {
        "identifier": 'ACTION_711_transfer_to_xyzf_32',
        "command": 'transfer_to_xyzf',
        "args": [12, 70, 0, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_711_jump_to_subroutine_33',
        "command": 'jump_to_subroutine',
        "args": [0x8391]
    },
    {
        "identifier": 'ACTION_711_jmp_34',
        "command": 'jmp',
        "args": ['ACTION_707_set_priority_0']
    }
]
