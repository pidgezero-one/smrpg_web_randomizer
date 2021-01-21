from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_644_pause_0',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_644_jmp_if_bit_clear_1',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 1, 'ACTION_644_pause_0']
    },
    {
        "identifier": 'ACTION_644_set_priority_2',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_644_set_vram_priority_3',
        "command": 'set_vram_priority',
        "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
    },
    {
        "identifier": 'ACTION_644_set_object_memory_bits_4',
        "command": 'set_object_memory_bits',
        "args": [0x0e, bits=[0, 1]]
    },
    {
        "identifier": 'ACTION_644_pause_5',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_644_jmp_if_bit_clear_6',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 2, 'ACTION_644_pause_5']
    },
    {
        "identifier": 'ACTION_644_pause_7',
        "command": 'pause',
        "args": [26]
    },
    {
        "identifier": 'ACTION_644_set_object_memory_bits_8',
        "command": 'set_object_memory_bits',
        "args": [0x0e, bits=[0]]
    },
    {
        "identifier": 'ACTION_644_object_memory_modify_bits_9',
        "command": 'object_memory_modify_bits',
        "args": [0x09, [5], [4, 6]]
    },
    {
        "identifier": 'ACTION_644_pause_10',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_644_jmp_if_bit_set_11',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 2, 'ACTION_644_pause_10']
    },
    {
        "identifier": 'ACTION_644_set_object_memory_bits_12',
        "command": 'set_object_memory_bits',
        "args": [0x0e, bits=[]]
    },
    {
        "identifier": 'ACTION_644_set_animation_speed_13',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_644_set_priority_14',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_644_jump_to_height_15',
        "command": 'jump_to_height',
        "args": [153]
    },
    {
        "identifier": 'ACTION_644_set_vram_priority_16',
        "command": 'set_vram_priority',
        "args": [VramPriority.PRIORITY_3]
    },
    {
        "identifier": 'ACTION_644_bounce_to_xy_with_height_17',
        "command": 'bounce_to_xy_with_height',
        "args": [17, 58, 0]
    },
    {
        "identifier": 'ACTION_644_set_animation_speed_18',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_644_add_z_coord_1_step_19',
        "command": 'add_z_coord_1_step'
    },
    {
        "identifier": 'ACTION_644_set_object_memory_bits_20',
        "command": 'set_object_memory_bits',
        "args": [0x0e, bits=[1]]
    },
    {
        "identifier": 'ACTION_644_pause_21',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_644_jmp_if_bit_clear_22',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 3, 'ACTION_644_pause_21']
    },
    {
        "identifier": 'ACTION_644_set_animation_speed_23',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_644_jump_to_height_24',
        "command": 'jump_to_height',
        "args": [48]
    },
    {
        "identifier": 'ACTION_644_shift_northeast_steps_25',
        "command": 'shift_northeast_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_644_pause_26',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_644_jmp_if_bit_clear_27',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 2, 'ACTION_644_pause_26']
    },
    {
        "identifier": 'ACTION_644_jump_to_height_28',
        "command": 'jump_to_height',
        "args": [80]
    },
    {
        "identifier": 'ACTION_644_pause_29',
        "command": 'pause',
        "args": [17]
    },
    {
        "identifier": 'ACTION_644_floating_off_30',
        "command": 'floating_off'
    },
    {
        "identifier": 'ACTION_644_set_object_memory_bits_31',
        "command": 'set_object_memory_bits',
        "args": [0x0e, bits=[0]]
    },
    {
        "identifier": 'ACTION_644_pause_32',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_644_jmp_if_bit_clear_33',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 1, 'ACTION_644_pause_32']
    },
    {
        "identifier": 'ACTION_644_set_object_memory_bits_34',
        "command": 'set_object_memory_bits',
        "args": [0x0e, bits=[0, 1]]
    },
    {
        "identifier": 'ACTION_644_pause_35',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_644_jmp_if_bit_clear_36',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 2, 'ACTION_644_pause_35']
    },
    {
        "identifier": 'ACTION_644_pause_37',
        "command": 'pause',
        "args": [13]
    },
    {
        "identifier": 'ACTION_644_set_object_memory_bits_38',
        "command": 'set_object_memory_bits',
        "args": [0x0e, bits=[]]
    },
    {
        "identifier": 'ACTION_644_jump_to_height_39',
        "command": 'jump_to_height',
        "args": [16]
    },
    {
        "identifier": 'ACTION_644_pause_40',
        "command": 'pause',
        "args": [14]
    },
    {
        "identifier": 'ACTION_644_floating_off_41',
        "command": 'floating_off'
    },
    {
        "identifier": 'ACTION_644_pause_42',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'ACTION_644_set_object_memory_bits_43',
        "command": 'set_object_memory_bits',
        "args": [0x0e, bits=[0]]
    },
    {
        "identifier": 'ACTION_644_pause_44',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_644_jmp_if_bit_clear_45',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 1, 'ACTION_644_pause_44']
    },
    {
        "identifier": 'ACTION_644_pause_46',
        "command": 'pause',
        "args": [13]
    },
    {
        "identifier": 'ACTION_644_set_object_memory_bits_47',
        "command": 'set_object_memory_bits',
        "args": [0x0e, bits=[]]
    },
    {
        "identifier": 'ACTION_644_jump_to_height_48',
        "command": 'jump_to_height',
        "args": [96]
    },
    {
        "identifier": 'ACTION_644_jmp_if_bit_set_49',
        "command": 'jmp_if_bit_set',
        "args": [0x7078, 4, 'ACTION_644_shift_southwest_steps_63']
    },
    {
        "identifier": 'ACTION_644_shift_southeast_steps_50',
        "command": 'shift_southeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_644_pause_51',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'ACTION_644_set_object_memory_bits_52',
        "command": 'set_object_memory_bits',
        "args": [0x0e, bits=[2, 3]]
    },
    {
        "identifier": 'ACTION_644_play_sound_53',
        "command": 'play_sound',
        "args": [Sounds._085_FLOWER, 4]
    },
    {
        "identifier": 'ACTION_644_start_loop_n_times_54',
        "command": 'start_loop_n_times',
        "args": [7]
    },
    {
        "identifier": 'ACTION_644_visibility_on_55',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_644_pause_56',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_644_visibility_off_57',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_644_pause_58',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_644_end_loop_59',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_644_set_bit_60',
        "command": 'set_bit',
        "args": [0x7078, 4]
    },
    {
        "identifier": 'ACTION_644_set_bit_61',
        "command": 'set_bit',
        "args": [0x7043, 4]
    },
    {
        "identifier": 'ACTION_644_ret_62',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_644_shift_southwest_steps_63',
        "command": 'shift_southwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_644_set_animation_speed_64',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_644_walk_1_step_south_65',
        "command": 'walk_1_step_south'
    },
    {
        "identifier": 'ACTION_644_walk_1_step_southwest_66',
        "command": 'walk_1_step_southwest'
    },
    {
        "identifier": 'ACTION_644_walk_1_step_south_67',
        "command": 'walk_1_step_south'
    },
    {
        "identifier": 'ACTION_644_visibility_off_68',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_644_clear_bit_69',
        "command": 'clear_bit',
        "args": [0x7043, 4]
    },
    {
        "identifier": 'ACTION_644_ret_70',
        "command": 'ret'
    }
]
