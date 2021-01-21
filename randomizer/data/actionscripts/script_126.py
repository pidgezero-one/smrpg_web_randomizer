from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_126_object_memory_set_bit_0',
        "command": 'object_memory_set_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_126_object_memory_set_bit_1',
        "command": 'object_memory_set_bit',
        "args": [0x0b, [3]]
    },
    {
        "identifier": 'ACTION_126_sequence_looping_on_2',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_126_set_priority_3',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_126_pause_4',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_126_set_700C_to_pressed_button_5',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_126_add_6',
        "command": 'add',
        "args": [0x700c, 65511]
    },
    {
        "identifier": 'ACTION_126_add_7',
        "command": 'add',
        "args": [0x700c, 25]
    },
    {
        "identifier": 'ACTION_126_jmp_if_mem_704x_at_700C_bit_set_8',
        "command": 'jmp_if_mem_704x_at_700C_bit_set',
        "args": ['ACTION_126_pause_4']
    },
    {
        "identifier": 'ACTION_126_add_9',
        "command": 'add',
        "args": [0x700c, 65511]
    },
    {
        "identifier": 'ACTION_126_mem_700C_and_const_10',
        "command": 'mem_700C_and_const',
        "args": [0x0003]
    },
    {
        "identifier": 'ACTION_126_add_11',
        "command": 'add',
        "args": [0x700c, 21]
    },
    {
        "identifier": 'ACTION_126_set_short_mem_12',
        "command": 'set_short_mem',
        "args": [0x70aa, 0x700c]
    },
    {
        "identifier": 'ACTION_126_db_13',
        "command": 'db',
        "args": [0x97, 0x12]
    },
    {
        "identifier": 'ACTION_126_jmp_if_bit_set_14',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 1, 'ACTION_126_pause_4']
    },
    {
        "identifier": 'ACTION_126_set_bit_15',
        "command": 'set_bit',
        "args": [0x7044, 1]
    },
    {
        "identifier": 'ACTION_126_set_animation_speed_16',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FASTER, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_126_play_sound_17',
        "command": 'play_sound',
        "args": [Sounds._033_JUMPING_BOUNCING_FISH, 4]
    },
    {
        "identifier": 'ACTION_126_set_short_18',
        "command": 'set_short',
        "args": [0x7034, 0xeeee]
    },
    {
        "identifier": 'ACTION_126_create_packet_at_object_coords_jmp_if_null_19',
        "command": 'create_packet_at_object_coords_jmp_if_null',
        "args": [NPCPackets._032_BLUE_CLOUD, AreaObjects.DUMMY_0X07, 'ACTION_126_jump_to_height_20']
    },
    {
        "identifier": 'ACTION_126_jump_to_height_20',
        "command": 'jump_to_height',
        "args": [188]
    },
    {
        "identifier": 'ACTION_126_pause_21',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_126_visibility_on_22',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_126_clear_bit_23',
        "command": 'clear_bit',
        "args": [0x7044, 1]
    },
    {
        "identifier": 'ACTION_126_shift_northwest_steps_24',
        "command": 'shift_northwest_steps',
        "args": [6]
    },
    {
        "identifier": 'ACTION_126_object_memory_clear_bit_25',
        "command": 'object_memory_clear_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_126_set_solidity_bits_26',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_126_pause_27',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_126_db_28',
        "command": 'db',
        "args": [0xfd, 0x3d, 0x07, 0xf3, 0x1b]
    },
    {
        "identifier": 'ACTION_126_set_animation_speed_29',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_126_floating_off_30',
        "command": 'floating_off'
    },
    {
        "identifier": 'ACTION_126_clear_solidity_bits_31',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_126_pause_32',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'ACTION_126_start_loop_n_times_33',
        "command": 'start_loop_n_times',
        "args": [7]
    },
    {
        "identifier": 'ACTION_126_walk_1_step_f_direction_34',
        "command": 'walk_1_step_f_direction'
    },
    {
        "identifier": 'ACTION_126_turn_clockwise_45_degrees_n_times_35',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [2]
    },
    {
        "identifier": 'ACTION_126_end_loop_36',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_126_walk_1_step_southwest_37',
        "command": 'walk_1_step_southwest'
    },
    {
        "identifier": 'ACTION_126_shift_southwest_pixels_38',
        "command": 'shift_southwest_pixels',
        "args": [2]
    },
    {
        "identifier": 'ACTION_126_floating_on_39',
        "command": 'floating_on'
    },
    {
        "identifier": 'ACTION_126_set_solidity_bits_40',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_126_pause_41',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_126_db_42',
        "command": 'db',
        "args": [0xfd, 0x3d, 0x07, 0x0f, 0x1c]
    },
    {
        "identifier": 'ACTION_126_floating_off_43',
        "command": 'floating_off'
    },
    {
        "identifier": 'ACTION_126_clear_solidity_bits_44',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_126_walk_1_step_southeast_45',
        "command": 'walk_1_step_southeast'
    },
    {
        "identifier": 'ACTION_126_floating_on_46',
        "command": 'floating_on'
    },
    {
        "identifier": 'ACTION_126_pause_47',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_126_db_48',
        "command": 'db',
        "args": [0xfd, 0x3d, 0x07, 0x1d, 0x1c]
    },
    {
        "identifier": 'ACTION_126_shift_southeast_steps_49',
        "command": 'shift_southeast_steps',
        "args": [4]
    },
    {
        "identifier": 'ACTION_126_walk_1_step_northeast_50',
        "command": 'walk_1_step_northeast'
    },
    {
        "identifier": 'ACTION_126_shift_northwest_steps_51',
        "command": 'shift_northwest_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_126_walk_1_step_southwest_52',
        "command": 'walk_1_step_southwest'
    },
    {
        "identifier": 'ACTION_126_shift_southeast_steps_53',
        "command": 'shift_southeast_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_126_shift_northeast_pixels_54',
        "command": 'shift_northeast_pixels',
        "args": [2]
    },
    {
        "identifier": 'ACTION_126_fixed_f_coord_on_55',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_126_pause_56',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'ACTION_126_set_animation_speed_57',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_126_jump_to_height_58',
        "command": 'jump_to_height',
        "args": [108]
    },
    {
        "identifier": 'ACTION_126_walk_1_step_east_59',
        "command": 'walk_1_step_east'
    },
    {
        "identifier": 'ACTION_126_pause_60',
        "command": 'pause',
        "args": [6]
    },
    {
        "identifier": 'ACTION_126_set_vram_priority_61',
        "command": 'set_vram_priority',
        "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
    },
    {
        "identifier": 'ACTION_126_pause_62',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_126_set_vram_priority_63',
        "command": 'set_vram_priority',
        "args": [VramPriority.NORMAL]
    },
    {
        "identifier": 'ACTION_126_fixed_f_coord_off_64',
        "command": 'fixed_f_coord_off'
    },
    {
        "identifier": 'ACTION_126_visibility_off_65',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_126_pause_66',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_126_db_67',
        "command": 'db',
        "args": [0xfd, 0x3d, 0x07, 0x41, 0x1c]
    },
    {
        "identifier": 'ACTION_126_pause_68',
        "command": 'pause',
        "args": [6]
    },
    {
        "identifier": 'ACTION_126_jmp_69',
        "command": 'jmp',
        "args": ['ACTION_126_pause_4']
    }
]
