from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_826_set_priority_0',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_826_set_700C_to_current_level_1',
        "command": 'set_700C_to_current_level'
    },
    {
        "identifier": 'ACTION_826_jmp_if_var_equals_short_2',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 473, 'ACTION_826_set_solidity_bits_61']
    },
    {
        "identifier": 'ACTION_826_set_700C_to_pressed_button_3',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_826_mem_compare_4',
        "command": 'mem_compare',
        "args": [0x700c, 24]
    },
    {
        "identifier": 'ACTION_826_jmp_if_comparison_result_is_greater_or_equal_5',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['ACTION_826_shift_f_direction_steps_55']
    },
    {
        "identifier": 'ACTION_826_jmp_if_var_equals_short_6',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 22, 'ACTION_826_shadow_on_34']
    },
    {
        "identifier": 'ACTION_826_shadow_on_7',
        "command": 'shadow_on'
    },
    {
        "identifier": 'ACTION_826_visibility_off_8',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_826_floating_off_9',
        "command": 'floating_off'
    },
    {
        "identifier": 'ACTION_826_set_solidity_bits_10',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_826_pause_11',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'ACTION_826_transfer_to_xyzf_12',
        "command": 'transfer_to_xyzf',
        "args": [7, 38, 2, RadialDirections.SOUTHEAST]
    },
    {
        "identifier": 'ACTION_826_face_southwest_13',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_826_jump_to_height_14',
        "command": 'jump_to_height',
        "args": [96]
    },
    {
        "identifier": 'ACTION_826_pause_15',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'ACTION_826_floating_on_16',
        "command": 'floating_on'
    },
    {
        "identifier": 'ACTION_826_visibility_on_17',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_826_object_memory_clear_bit_18',
        "command": 'object_memory_clear_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_826_pause_19',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'ACTION_826_play_sound_20',
        "command": 'play_sound',
        "args": [Sounds._022_CLOSE_DOOR, 4]
    },
    {
        "identifier": 'ACTION_826_pause_21',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_826_jump_to_height_22',
        "command": 'jump_to_height',
        "args": [64]
    },
    {
        "identifier": 'ACTION_826_walk_1_step_southwest_23',
        "command": 'walk_1_step_southwest'
    },
    {
        "identifier": 'ACTION_826_pause_24',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'ACTION_826_play_sound_25',
        "command": 'play_sound',
        "args": [Sounds._022_CLOSE_DOOR, 4]
    },
    {
        "identifier": 'ACTION_826_pause_26',
        "command": 'pause',
        "args": [58]
    },
    {
        "identifier": 'ACTION_826_play_sound_27',
        "command": 'play_sound',
        "args": [Sounds._022_CLOSE_DOOR, 4]
    },
    {
        "identifier": 'ACTION_826_jump_to_height_28',
        "command": 'jump_to_height',
        "args": [96]
    },
    {
        "identifier": 'ACTION_826_clear_solidity_bits_29',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_826_walk_1_step_southeast_30',
        "command": 'walk_1_step_southeast'
    },
    {
        "identifier": 'ACTION_826_shadow_off_31',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_826_walk_1_step_southeast_32',
        "command": 'walk_1_step_southeast'
    },
    {
        "identifier": 'ACTION_826_jmp_33',
        "command": 'jmp',
        "args": ['ACTION_826_shadow_on_7']
    },
    {
        "identifier": 'ACTION_826_shadow_on_34',
        "command": 'shadow_on'
    },
    {
        "identifier": 'ACTION_826_visibility_off_35',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_826_floating_off_36',
        "command": 'floating_off'
    },
    {
        "identifier": 'ACTION_826_set_solidity_bits_37',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_826_pause_38',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'ACTION_826_transfer_to_xyzf_39',
        "command": 'transfer_to_xyzf',
        "args": [14, 24, 0, RadialDirections.SOUTHEAST]
    },
    {
        "identifier": 'ACTION_826_jump_to_height_40',
        "command": 'jump_to_height',
        "args": [96]
    },
    {
        "identifier": 'ACTION_826_pause_41',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'ACTION_826_floating_on_42',
        "command": 'floating_on'
    },
    {
        "identifier": 'ACTION_826_visibility_on_43',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_826_object_memory_clear_bit_44',
        "command": 'object_memory_clear_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_826_pause_45',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'ACTION_826_play_sound_46',
        "command": 'play_sound',
        "args": [Sounds._022_CLOSE_DOOR, 4]
    },
    {
        "identifier": 'ACTION_826_pause_47',
        "command": 'pause',
        "args": [42]
    },
    {
        "identifier": 'ACTION_826_play_sound_48',
        "command": 'play_sound',
        "args": [Sounds._022_CLOSE_DOOR, 4]
    },
    {
        "identifier": 'ACTION_826_pause_49',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_826_jump_to_height_50',
        "command": 'jump_to_height',
        "args": [96]
    },
    {
        "identifier": 'ACTION_826_clear_solidity_bits_51',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_826_shadow_off_52',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_826_shift_southwest_steps_53',
        "command": 'shift_southwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_826_jmp_54',
        "command": 'jmp',
        "args": ['ACTION_826_shadow_on_34']
    },
    {
        "identifier": 'ACTION_826_shift_f_direction_steps_55',
        "command": 'shift_f_direction_steps',
        "args": [4]
    },
    {
        "identifier": 'ACTION_826_pause_56',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_826_turn_clockwise_45_degrees_n_times_57',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [2]
    },
    {
        "identifier": 'ACTION_826_pause_58',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_826_turn_clockwise_45_degrees_n_times_59',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [2]
    },
    {
        "identifier": 'ACTION_826_jmp_60',
        "command": 'jmp',
        "args": ['ACTION_826_shift_f_direction_steps_55']
    },
    {
        "identifier": 'ACTION_826_set_solidity_bits_61',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_826_set_700C_to_pressed_button_62',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_826_add_63',
        "command": 'add',
        "args": [0x700c, 65517]
    },
    {
        "identifier": 'ACTION_826_load_mem_64',
        "command": 'load_mem',
        "args": [0x700c]
    },
    {
        "identifier": 'ACTION_826_pause_65',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_826_end_loop_66',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_826_set_animation_speed_67',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_826_fixed_f_coord_on_68',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_826_start_loop_n_times_69',
        "command": 'start_loop_n_times',
        "args": [2]
    },
    {
        "identifier": 'ACTION_826_walk_1_step_southeast_70',
        "command": 'walk_1_step_southeast'
    },
    {
        "identifier": 'ACTION_826_pause_71',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_826_end_loop_72',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_826_start_loop_n_times_73',
        "command": 'start_loop_n_times',
        "args": [2]
    },
    {
        "identifier": 'ACTION_826_walk_1_step_northwest_74',
        "command": 'walk_1_step_northwest'
    },
    {
        "identifier": 'ACTION_826_pause_75',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_826_end_loop_76',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_826_jmp_77',
        "command": 'jmp',
        "args": ['ACTION_826_start_loop_n_times_69']
    }
]
