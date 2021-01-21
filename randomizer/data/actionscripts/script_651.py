from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_651_sequence_looping_on_0',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_651_jmp_if_var_equals_short_1',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7034, 65535, 'ACTION_651_set_priority_22']
    },
    {
        "identifier": 'ACTION_651_jmp_if_var_equals_short_2',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7034, 61166, 'ACTION_651_visibility_off_19']
    },
    {
        "identifier": 'ACTION_651_jmp_if_var_equals_short_3',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7034, 56797, 'ACTION_651_set_animation_speed_31']
    },
    {
        "identifier": 'ACTION_651_jmp_if_var_equals_short_4',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7034, 52428, 'ACTION_651_set_priority_38']
    },
    {
        "identifier": 'ACTION_651_set_short_mem_5',
        "command": 'set_short_mem',
        "args": [0x700c, 0x7034]
    },
    {
        "identifier": 'ACTION_651_mem_compare_6',
        "command": 'mem_compare',
        "args": [0x700c, 32768]
    },
    {
        "identifier": 'ACTION_651_jmp_if_comparison_result_is_lesser_7',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['ACTION_651_face_east_10']
    },
    {
        "identifier": 'ACTION_651_mem_700C_and_const_8',
        "command": 'mem_700C_and_const',
        "args": [0x00ff]
    },
    {
        "identifier": 'ACTION_651_set_vram_priority_9',
        "command": 'set_vram_priority',
        "args": [VramPriority.PRIORITY_3]
    },
    {
        "identifier": 'ACTION_651_face_east_10',
        "command": 'face_east'
    },
    {
        "identifier": 'ACTION_651_set_animation_speed_11',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_651_set_animation_speed_12',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_651_set_priority_13',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_651_shift_f_direction_pixels_14',
        "command": 'shift_f_direction_pixels',
        "args": [12]
    },
    {
        "identifier": 'ACTION_651_set_sprite_sequence_15',
        "command": 'set_sprite_sequence',
        "args": [1, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_651_shift_f_direction_pixels_16',
        "command": 'shift_f_direction_pixels',
        "args": [4]
    },
    {
        "identifier": 'ACTION_651_visibility_off_17',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_651_ret_18',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_651_visibility_off_19',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_651_transfer_xyzf_pixels_20',
        "command": 'transfer_xyzf_pixels',
        "args": [0, 0, 24, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_651_visibility_on_21',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_651_set_priority_22',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_651_set_vram_priority_23',
        "command": 'set_vram_priority',
        "args": [VramPriority.PRIORITY_3]
    },
    {
        "identifier": 'ACTION_651_set_animation_speed_24',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_651_set_animation_speed_25',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_651_shift_z_up_pixels_26',
        "command": 'shift_z_up_pixels',
        "args": [12]
    },
    {
        "identifier": 'ACTION_651_set_sprite_sequence_27',
        "command": 'set_sprite_sequence',
        "args": [1, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_651_shift_z_up_pixels_28',
        "command": 'shift_z_up_pixels',
        "args": [4]
    },
    {
        "identifier": 'ACTION_651_visibility_off_29',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_651_ret_30',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_651_set_animation_speed_31',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_651_set_animation_speed_32',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_651_shift_z_up_pixels_33',
        "command": 'shift_z_up_pixels',
        "args": [12]
    },
    {
        "identifier": 'ACTION_651_set_sprite_sequence_34',
        "command": 'set_sprite_sequence',
        "args": [1, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_651_shift_z_up_pixels_35',
        "command": 'shift_z_up_pixels',
        "args": [4]
    },
    {
        "identifier": 'ACTION_651_visibility_off_36',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_651_ret_37',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_651_set_priority_38',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_651_set_solidity_bits_39',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_651_shadow_on_40',
        "command": 'shadow_on'
    },
    {
        "identifier": 'ACTION_651_set_solidity_bits_41',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_651_set_animation_speed_42',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_651_db_43',
        "command": 'db',
        "args": [0x3a, 0x00, 0x00, 0x04, 0x45, 0x77]
    },
    {
        "identifier": 'ACTION_651_set_animation_speed_44',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_651_turn_random_direction_45',
        "command": 'turn_random_direction'
    },
    {
        "identifier": 'ACTION_651_walk_1_step_f_direction_46',
        "command": 'walk_1_step_f_direction'
    },
    {
        "identifier": 'ACTION_651_jmp_47',
        "command": 'jmp',
        "args": ['ACTION_651_db_43']
    },
    {
        "identifier": 'ACTION_651_face_mario_48',
        "command": 'face_mario'
    },
    {
        "identifier": 'ACTION_651_set_animation_speed_49',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_651_turn_clockwise_45_degrees_n_times_50',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [4]
    },
    {
        "identifier": 'ACTION_651_walk_1_step_f_direction_51',
        "command": 'walk_1_step_f_direction'
    },
    {
        "identifier": 'ACTION_651_turn_clockwise_45_degrees_n_times_52',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [4]
    },
    {
        "identifier": 'ACTION_651_pause_53',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'ACTION_651_jmp_if_random_above_66_54',
        "command": 'jmp_if_random_above_66',
        "args": ['ACTION_651_turn_clockwise_45_degrees_n_times_57']
    },
    {
        "identifier": 'ACTION_651_turn_clockwise_45_degrees_n_times_55',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [3]
    },
    {
        "identifier": 'ACTION_651_jmp_56',
        "command": 'jmp',
        "args": ['ACTION_651_walk_1_step_f_direction_60']
    },
    {
        "identifier": 'ACTION_651_turn_clockwise_45_degrees_n_times_57',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [4]
    },
    {
        "identifier": 'ACTION_651_jmp_58',
        "command": 'jmp',
        "args": ['ACTION_651_walk_1_step_f_direction_60']
    },
    {
        "identifier": 'ACTION_651_turn_clockwise_45_degrees_n_times_59',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [5]
    },
    {
        "identifier": 'ACTION_651_walk_1_step_f_direction_60',
        "command": 'walk_1_step_f_direction'
    },
    {
        "identifier": 'ACTION_651_jmp_61',
        "command": 'jmp',
        "args": ['ACTION_651_db_43']
    }
]
