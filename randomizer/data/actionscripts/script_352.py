from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_352_object_memory_clear_bit_0',
        "command": 'object_memory_clear_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_352_set_short_1',
        "command": 'set_short',
        "args": [0x701e, 0x0190]
    },
    {
        "identifier": 'ACTION_352_set_vram_priority_2',
        "command": 'set_vram_priority',
        "args": [VramPriority.NORMAL]
    },
    {
        "identifier": 'ACTION_352_set_animation_speed_3',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FASTER, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_352_set_animation_speed_4',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_352_jmp_if_var_not_equals_byte_5',
        "command": 'jmp_if_var_not_equals_byte',
        "args": [0x70af, 0, 'ACTION_352_dec_14']
    },
    {
        "identifier": 'ACTION_352_set_6',
        "command": 'set',
        "args": [0x70af, 3]
    },
    {
        "identifier": 'ACTION_352_clear_bit_7',
        "command": 'clear_bit',
        "args": [0x7044, 0]
    },
    {
        "identifier": 'ACTION_352_dec_short_8',
        "command": 'dec_short',
        "args": [0x702c]
    },
    {
        "identifier": 'ACTION_352_jmp_if_var_not_equals_short_9',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x702c, 0, 'ACTION_352_jmp_if_bit_set_13']
    },
    {
        "identifier": 'ACTION_352_set_short_10',
        "command": 'set_short',
        "args": [0x702e, 0x0080]
    },
    {
        "identifier": 'ACTION_352_set_sprite_sequence_11',
        "command": 'set_sprite_sequence',
        "args": [5, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_352_jmp_12',
        "command": 'jmp',
        "args": ['ACTION_352_visibility_on_27']
    },
    {
        "identifier": 'ACTION_352_jmp_if_bit_set_13',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 6, 'ACTION_352_ret_68']
    },
    {
        "identifier": 'ACTION_352_dec_14',
        "command": 'dec',
        "args": [0x70af]
    },
    {
        "identifier": 'ACTION_352_set_random_15',
        "command": 'set_random',
        "args": [0x700c, 65535]
    },
    {
        "identifier": 'ACTION_352_jmp_if_var_not_equals_byte_16',
        "command": 'jmp_if_var_not_equals_byte',
        "args": [0x70af, 0, 'ACTION_352_jmp_if_700C_all_bits_clear_19']
    },
    {
        "identifier": 'ACTION_352_jmp_if_bit_set_17',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 0, 'ACTION_352_set_short_25']
    },
    {
        "identifier": 'ACTION_352_jmp_18',
        "command": 'jmp',
        "args": ['ACTION_352_set_bit_21']
    },
    {
        "identifier": 'ACTION_352_jmp_if_700C_all_bits_clear_19',
        "command": 'jmp_if_700C_all_bits_clear',
        "args": [[0], 'ACTION_352_set_short_25']
    },
    {
        "identifier": 'ACTION_352_jmp_if_bit_set_20',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 0, 'ACTION_352_set_short_25']
    },
    {
        "identifier": 'ACTION_352_set_bit_21',
        "command": 'set_bit',
        "args": [0x7044, 0]
    },
    {
        "identifier": 'ACTION_352_set_short_22',
        "command": 'set_short',
        "args": [0x702e, 0x0010]
    },
    {
        "identifier": 'ACTION_352_set_sprite_sequence_23',
        "command": 'set_sprite_sequence',
        "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_352_jmp_24',
        "command": 'jmp',
        "args": ['ACTION_352_visibility_on_27']
    },
    {
        "identifier": 'ACTION_352_set_short_25',
        "command": 'set_short',
        "args": [0x702e, 0x0001]
    },
    {
        "identifier": 'ACTION_352_set_sprite_sequence_26',
        "command": 'set_sprite_sequence',
        "args": [3, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_352_visibility_on_27',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_352_mem_compare_28',
        "command": 'mem_compare',
        "args": [0x700c, 24576]
    },
    {
        "identifier": 'ACTION_352_jmp_if_comparison_result_is_lesser_29',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['ACTION_352_transfer_to_xyzf_36']
    },
    {
        "identifier": 'ACTION_352_mem_compare_30',
        "command": 'mem_compare',
        "args": [0x700c, 45056]
    },
    {
        "identifier": 'ACTION_352_jmp_if_comparison_result_is_lesser_31',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['ACTION_352_transfer_to_xyzf_40']
    },
    {
        "identifier": 'ACTION_352_transfer_to_xyzf_32',
        "command": 'transfer_to_xyzf',
        "args": [1, 50, 7, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_352_shift_southeast_steps_33',
        "command": 'shift_southeast_steps',
        "args": [7]
    },
    {
        "identifier": 'ACTION_352_set_animation_speed_34',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_352_jmp_35',
        "command": 'jmp',
        "args": ['ACTION_352_pause_60']
    },
    {
        "identifier": 'ACTION_352_transfer_to_xyzf_36',
        "command": 'transfer_to_xyzf',
        "args": [2, 48, 7, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_352_shift_southeast_steps_37',
        "command": 'shift_southeast_steps',
        "args": [7]
    },
    {
        "identifier": 'ACTION_352_set_animation_speed_38',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_352_jmp_39',
        "command": 'jmp',
        "args": ['ACTION_352_jmp_if_random_above_128_44']
    },
    {
        "identifier": 'ACTION_352_transfer_to_xyzf_40',
        "command": 'transfer_to_xyzf',
        "args": [3, 46, 7, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_352_shift_southeast_steps_41',
        "command": 'shift_southeast_steps',
        "args": [7]
    },
    {
        "identifier": 'ACTION_352_set_animation_speed_42',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_352_jmp_43',
        "command": 'jmp',
        "args": ['ACTION_352_pause_55']
    },
    {
        "identifier": 'ACTION_352_jmp_if_random_above_128_44',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_352_pause_50']
    },
    {
        "identifier": 'ACTION_352_pause_45',
        "command": 'pause',
        "args": [6]
    },
    {
        "identifier": 'ACTION_352_shift_northeast_steps_46',
        "command": 'shift_northeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_352_mem_compare_47',
        "command": 'mem_compare',
        "args": [0x702a, 170]
    },
    {
        "identifier": 'ACTION_352_jmp_if_comparison_result_is_lesser_48',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['ACTION_352_set_animation_speed_65']
    },
    {
        "identifier": 'ACTION_352_jmp_49',
        "command": 'jmp',
        "args": ['ACTION_352_pause_55']
    },
    {
        "identifier": 'ACTION_352_pause_50',
        "command": 'pause',
        "args": [6]
    },
    {
        "identifier": 'ACTION_352_shift_southwest_steps_51',
        "command": 'shift_southwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_352_mem_compare_52',
        "command": 'mem_compare',
        "args": [0x702a, 170]
    },
    {
        "identifier": 'ACTION_352_jmp_if_comparison_result_is_lesser_53',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['ACTION_352_set_animation_speed_65']
    },
    {
        "identifier": 'ACTION_352_jmp_54',
        "command": 'jmp',
        "args": ['ACTION_352_pause_60']
    },
    {
        "identifier": 'ACTION_352_pause_55',
        "command": 'pause',
        "args": [6]
    },
    {
        "identifier": 'ACTION_352_shift_southwest_steps_56',
        "command": 'shift_southwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_352_mem_compare_57',
        "command": 'mem_compare',
        "args": [0x702a, 170]
    },
    {
        "identifier": 'ACTION_352_jmp_if_comparison_result_is_lesser_58',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['ACTION_352_set_animation_speed_65']
    },
    {
        "identifier": 'ACTION_352_jmp_59',
        "command": 'jmp',
        "args": ['ACTION_352_jmp_if_random_above_128_44']
    },
    {
        "identifier": 'ACTION_352_pause_60',
        "command": 'pause',
        "args": [6]
    },
    {
        "identifier": 'ACTION_352_shift_northeast_steps_61',
        "command": 'shift_northeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_352_mem_compare_62',
        "command": 'mem_compare',
        "args": [0x702a, 170]
    },
    {
        "identifier": 'ACTION_352_jmp_if_comparison_result_is_lesser_63',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['ACTION_352_set_animation_speed_65']
    },
    {
        "identifier": 'ACTION_352_jmp_64',
        "command": 'jmp',
        "args": ['ACTION_352_jmp_if_random_above_128_44']
    },
    {
        "identifier": 'ACTION_352_set_animation_speed_65',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_352_shift_northwest_steps_66',
        "command": 'shift_northwest_steps',
        "args": [7]
    },
    {
        "identifier": 'ACTION_352_jmp_67',
        "command": 'jmp',
        "args": ['ACTION_352_object_memory_clear_bit_0']
    },
    {
        "identifier": 'ACTION_352_ret_68',
        "command": 'ret'
    }
]
