from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_60_set_priority_0',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_60_set_700C_to_pressed_button_1',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_60_mem_700C_and_const_2',
        "command": 'mem_700C_and_const',
        "args": [0x0003]
    },
    {
        "identifier": 'ACTION_60_jmp_if_700C_equals_short_3',
        "command": 'jmp_if_700C_equals_short',
        "args": [1, 'ACTION_60_pause_7']
    },
    {
        "identifier": 'ACTION_60_jmp_if_700C_equals_short_4',
        "command": 'jmp_if_700C_equals_short',
        "args": [2, 'ACTION_60_pause_8']
    },
    {
        "identifier": 'ACTION_60_jmp_if_700C_equals_short_5',
        "command": 'jmp_if_700C_equals_short',
        "args": [3, 'ACTION_60_pause_9']
    },
    {
        "identifier": 'ACTION_60_pause_6',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'ACTION_60_pause_7',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'ACTION_60_pause_8',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'ACTION_60_pause_9',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'ACTION_60_object_memory_set_bit_10',
        "command": 'object_memory_set_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_60_clear_solidity_bits_11',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_60_visibility_off_12',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_60_turn_random_direction_13',
        "command": 'turn_random_direction'
    },
    {
        "identifier": 'ACTION_60_set_animation_speed_14',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_60_start_loop_n_times_15',
        "command": 'start_loop_n_times',
        "args": [2]
    },
    {
        "identifier": 'ACTION_60_set_700C_to_object_coord_16',
        "command": 'set_700C_to_object_coord',
        "args": [AreaObjects.MARIO, Coords.Z, [], CoordUnits.PIXEL]
    },
    {
        "identifier": 'ACTION_60_add_17',
        "command": 'add',
        "args": [0x700c, 224]
    },
    {
        "identifier": 'ACTION_60_set_7000_short_mem_to_700C_18',
        "command": 'set_7000_short_mem_to_700C',
        "args": [0x7028]
    },
    {
        "identifier": 'ACTION_60_set_700C_to_object_coord_19',
        "command": 'set_700C_to_object_coord',
        "args": [AreaObjects.DUMMY_0X07, Coords.Z, [], CoordUnits.PIXEL]
    },
    {
        "identifier": 'ACTION_60_mem_compare_address_20',
        "command": 'mem_compare_address',
        "args": [0x7028]
    },
    {
        "identifier": 'ACTION_60_jmp_if_loaded_memory_is_0_21',
        "command": 'jmp_if_loaded_memory_is_0',
        "args": ['ACTION_60_jmp_24']
    },
    {
        "identifier": 'ACTION_60_jmp_if_loaded_memory_is_below_0_22',
        "command": 'jmp_if_loaded_memory_is_below_0',
        "args": ['ACTION_60_shift_z_down_pixels_25']
    },
    {
        "identifier": 'ACTION_60_jmp_if_loaded_memory_is_above_or_equal_0_23',
        "command": 'jmp_if_loaded_memory_is_above_or_equal_0',
        "args": ['ACTION_60_shift_z_up_pixels_27']
    },
    {
        "identifier": 'ACTION_60_jmp_24',
        "command": 'jmp',
        "args": ['ACTION_60_walk_1_step_f_direction_28']
    },
    {
        "identifier": 'ACTION_60_shift_z_down_pixels_25',
        "command": 'shift_z_down_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_60_jmp_26',
        "command": 'jmp',
        "args": ['ACTION_60_walk_1_step_f_direction_28']
    },
    {
        "identifier": 'ACTION_60_shift_z_up_pixels_27',
        "command": 'shift_z_up_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_60_walk_1_step_f_direction_28',
        "command": 'walk_1_step_f_direction'
    },
    {
        "identifier": 'ACTION_60_end_loop_29',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_60_object_memory_clear_bit_30',
        "command": 'object_memory_clear_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_60_set_solidity_bits_31',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_60_reset_properties_32',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_60_play_sound_33',
        "command": 'play_sound',
        "args": [Sounds._044_GHOST_FLOAT, 4]
    },
    {
        "identifier": 'ACTION_60_start_loop_n_times_34',
        "command": 'start_loop_n_times',
        "args": [3]
    },
    {
        "identifier": 'ACTION_60_visibility_off_35',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_60_pause_36',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_60_visibility_on_37',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_60_pause_38',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_60_end_loop_39',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_60_face_mario_40',
        "command": 'face_mario'
    },
    {
        "identifier": 'ACTION_60_set_700C_to_object_coord_41',
        "command": 'set_700C_to_object_coord',
        "args": [AreaObjects.DUMMY_0X07, Coords.F, []]
    },
    {
        "identifier": 'ACTION_60_mem_700C_and_const_42',
        "command": 'mem_700C_and_const',
        "args": [0x0006]
    },
    {
        "identifier": 'ACTION_60_inc_43',
        "command": 'inc',
        "args": [0x700c]
    },
    {
        "identifier": 'ACTION_60_face_east_7C_44',
        "command": 'face_east_7C'
    },
    {
        "identifier": 'ACTION_60_sequence_looping_on_45',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_60_jmp_if_700C_equals_short_46',
        "command": 'jmp_if_700C_equals_short',
        "args": [1, 'ACTION_60_set_sprite_sequence_50']
    },
    {
        "identifier": 'ACTION_60_jmp_if_700C_equals_short_47',
        "command": 'jmp_if_700C_equals_short',
        "args": [3, 'ACTION_60_set_sprite_sequence_52']
    },
    {
        "identifier": 'ACTION_60_jmp_if_700C_equals_short_48',
        "command": 'jmp_if_700C_equals_short',
        "args": [5, 'ACTION_60_set_sprite_sequence_52']
    },
    {
        "identifier": 'ACTION_60_jmp_if_700C_equals_short_49',
        "command": 'jmp_if_700C_equals_short',
        "args": [7, 'ACTION_60_set_sprite_sequence_50']
    },
    {
        "identifier": 'ACTION_60_set_sprite_sequence_50',
        "command": 'set_sprite_sequence',
        "args": [3, 0, [_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_60_jmp_51',
        "command": 'jmp',
        "args": ['ACTION_60_set_animation_speed_53']
    },
    {
        "identifier": 'ACTION_60_set_sprite_sequence_52',
        "command": 'set_sprite_sequence',
        "args": [3, 0, [_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_60_set_animation_speed_53',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_60_shift_f_direction_steps_54',
        "command": 'shift_f_direction_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_60_sequence_looping_off_55',
        "command": 'sequence_looping_off'
    },
    {
        "identifier": 'ACTION_60_play_sound_56',
        "command": 'play_sound',
        "args": [Sounds._000_SILENCE, 6]
    },
    {
        "identifier": 'ACTION_60_start_loop_n_times_57',
        "command": 'start_loop_n_times',
        "args": [3]
    },
    {
        "identifier": 'ACTION_60_visibility_off_58',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_60_pause_59',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_60_visibility_on_60',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_60_pause_61',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_60_end_loop_62',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_60_visibility_off_63',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_60_jmp_64',
        "command": 'jmp',
        "args": ['ACTION_60_set_priority_0']
    }
]
