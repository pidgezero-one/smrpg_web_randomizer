from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_713_sequence_looping_on_0',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_713_set_sprite_sequence_1',
        "command": 'set_sprite_sequence',
        "args": [8, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_713_set_700C_to_current_level_2',
        "command": 'set_700C_to_current_level'
    },
    {
        "identifier": 'ACTION_713_jmp_if_700C_equals_short_3',
        "command": 'jmp_if_700C_equals_short',
        "args": [319, 'ACTION_713_pause_33']
    },
    {
        "identifier": 'ACTION_713_jmp_if_700C_equals_short_4',
        "command": 'jmp_if_700C_equals_short',
        "args": [403, 'ACTION_713_pause_33']
    },
    {
        "identifier": 'ACTION_713_set_priority_5',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_713_jmp_if_bit_set_6',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 4, 'ACTION_713_set_animation_speed_8']
    },
    {
        "identifier": 'ACTION_713_play_sound_7',
        "command": 'play_sound',
        "args": [Sounds._009_GREEN_SWITCH, 4]
    },
    {
        "identifier": 'ACTION_713_set_animation_speed_8',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_713_shift_z_up_pixels_9',
        "command": 'shift_z_up_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_713_shift_z_down_pixels_10',
        "command": 'shift_z_down_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_713_set_animation_speed_11',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_713_clear_bit_12',
        "command": 'clear_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'ACTION_713_clear_solidity_bits_13',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_713_visibility_off_14',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_713_set_15',
        "command": 'set',
        "args": [0x70ae, 0]
    },
    {
        "identifier": 'ACTION_713_pause_16',
        "command": 'pause',
        "args": [56]
    },
    {
        "identifier": 'ACTION_713_set_random_17',
        "command": 'set_random',
        "args": [0x700c, 8]
    },
    {
        "identifier": 'ACTION_713_inc_18',
        "command": 'inc',
        "args": [0x700c]
    },
    {
        "identifier": 'ACTION_713_load_mem_19',
        "command": 'load_mem',
        "args": [0x700c]
    },
    {
        "identifier": 'ACTION_713_pause_20',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_713_end_loop_21',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_713_play_sound_22',
        "command": 'play_sound',
        "args": [Sounds._009_GREEN_SWITCH, 4]
    },
    {
        "identifier": 'ACTION_713_set_animation_speed_23',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_713_set_bit_24',
        "command": 'set_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'ACTION_713_clear_bit_25',
        "command": 'clear_bit',
        "args": [0x7043, 4]
    },
    {
        "identifier": 'ACTION_713_visibility_on_26',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_713_set_solidity_bits_27',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_713_shift_z_up_pixels_28',
        "command": 'shift_z_up_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_713_shift_z_down_pixels_29',
        "command": 'shift_z_down_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_713_set_animation_speed_30',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_713_pause_31',
        "command": 'pause',
        "args": [100]
    },
    {
        "identifier": 'ACTION_713_jmp_32',
        "command": 'jmp',
        "args": ['ACTION_713_jmp_if_bit_set_6']
    },
    {
        "identifier": 'ACTION_713_pause_33',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_713_jmp_if_bit_clear_34',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 5, 'ACTION_713_pause_33']
    },
    {
        "identifier": 'ACTION_713_jmp_if_bit_set_35',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 4, 'ACTION_713_set_animation_speed_37']
    },
    {
        "identifier": 'ACTION_713_play_sound_36',
        "command": 'play_sound',
        "args": [Sounds._009_GREEN_SWITCH, 4]
    },
    {
        "identifier": 'ACTION_713_set_animation_speed_37',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_713_shift_z_up_pixels_38',
        "command": 'shift_z_up_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_713_shift_z_down_pixels_39',
        "command": 'shift_z_down_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_713_set_animation_speed_40',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_713_clear_bit_41',
        "command": 'clear_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'ACTION_713_clear_solidity_bits_42',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_713_visibility_off_43',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_713_set_44',
        "command": 'set',
        "args": [0x70ae, 0]
    },
    {
        "identifier": 'ACTION_713_set_random_45',
        "command": 'set_random',
        "args": [0x700c, 32768]
    },
    {
        "identifier": 'ACTION_713_set_7000_short_mem_to_700C_46',
        "command": 'set_7000_short_mem_to_700C',
        "args": [0x7034]
    },
    {
        "identifier": 'ACTION_713_mem_compare_val_47',
        "command": 'mem_compare_val',
        "args": [16384]
    },
    {
        "identifier": 'ACTION_713_jmp_if_comparison_result_is_lesser_48',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['ACTION_713_set_51']
    },
    {
        "identifier": 'ACTION_713_set_49',
        "command": 'set',
        "args": [0x700c, 1]
    },
    {
        "identifier": 'ACTION_713_jmp_50',
        "command": 'jmp',
        "args": ['ACTION_713_add_short_mem_52']
    },
    {
        "identifier": 'ACTION_713_set_51',
        "command": 'set',
        "args": [0x700c, 0]
    },
    {
        "identifier": 'ACTION_713_add_short_mem_52',
        "command": 'add_short_mem',
        "args": [0x700c, 0x7024]
    },
    {
        "identifier": 'ACTION_713_set_7000_short_mem_to_700C_53',
        "command": 'set_7000_short_mem_to_700C',
        "args": [0x7026]
    },
    {
        "identifier": 'ACTION_713_set_70A0_short_mem_to_700C_54',
        "command": 'set_70A0_short_mem_to_700C',
        "args": [0x70a9]
    },
    {
        "identifier": 'ACTION_713_object_memory_set_bit_55',
        "command": 'object_memory_set_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_713_set_bit_56',
        "command": 'set_bit',
        "args": [0x7044, 4]
    },
    {
        "identifier": 'ACTION_713_set_object_memory_bits_57',
        "command": 'set_object_memory_bits',
        "args": [0x0e, []]
    },
    {
        "identifier": 'ACTION_713_db_58',
        "command": 'db',
        "args": [0x97, 0x11]
    },
    {
        "identifier": 'ACTION_713_clear_bit_59',
        "command": 'clear_bit',
        "args": [0x7044, 4]
    },
    {
        "identifier": 'ACTION_713_object_memory_clear_bit_60',
        "command": 'object_memory_clear_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_713_set_700C_to_7000_short_mem_61',
        "command": 'set_700C_to_7000_short_mem',
        "args": [0x7026]
    },
    {
        "identifier": 'ACTION_713_dec_short_mem_62',
        "command": 'dec_short_mem',
        "args": [0x700c, 0x7024]
    },
    {
        "identifier": 'ACTION_713_jmp_if_700C_equals_short_63',
        "command": 'jmp_if_700C_equals_short',
        "args": [1, 'ACTION_713_set_object_memory_bits_66']
    },
    {
        "identifier": 'ACTION_713_set_object_memory_bits_64',
        "command": 'set_object_memory_bits',
        "args": [0x0e, [1]]
    },
    {
        "identifier": 'ACTION_713_jmp_65',
        "command": 'jmp',
        "args": ['ACTION_713_pause_67']
    },
    {
        "identifier": 'ACTION_713_set_object_memory_bits_66',
        "command": 'set_object_memory_bits',
        "args": [0x0e, [0]]
    },
    {
        "identifier": 'ACTION_713_pause_67',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_713_play_sound_68',
        "command": 'play_sound',
        "args": [Sounds._009_GREEN_SWITCH, 4]
    },
    {
        "identifier": 'ACTION_713_set_animation_speed_69',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_713_set_bit_70',
        "command": 'set_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'ACTION_713_clear_bit_71',
        "command": 'clear_bit',
        "args": [0x7043, 4]
    },
    {
        "identifier": 'ACTION_713_set_solidity_bits_72',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_713_visibility_on_73',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_713_shift_z_up_pixels_74',
        "command": 'shift_z_up_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_713_shift_z_down_pixels_75',
        "command": 'shift_z_down_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_713_set_animation_speed_76',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_713_pause_77',
        "command": 'pause',
        "args": [100]
    },
    {
        "identifier": 'ACTION_713_jmp_78',
        "command": 'jmp',
        "args": ['ACTION_713_jmp_if_bit_set_35']
    }
]
