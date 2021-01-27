from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_635_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 3, 'ACTION_635_transfer_to_xyzf_8']
    },
    {
        "identifier": 'ACTION_635_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 4, 'ACTION_635_transfer_to_xyzf_11']
    },
    {
        "identifier": 'ACTION_635_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 5, 'ACTION_635_transfer_to_xyzf_14']
    },
    {
        "identifier": 'ACTION_635_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 7, 'ACTION_635_transfer_to_xyzf_20']
    },
    {
        "identifier": 'ACTION_635_jmp_if_bit_set_4',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 1, 'ACTION_635_transfer_to_xyzf_17']
    },
    {
        "identifier": 'ACTION_635_transfer_to_xyzf_5',
        "command": 'transfer_to_xyzf',
        "args": [10, 59, 0, RadialDirections.SOUTHEAST]
    },
    {
        "identifier": 'ACTION_635_set_priority_6',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_635_jmp_7',
        "command": 'jmp',
        "args": ['ACTION_635_visibility_on_22']
    },
    {
        "identifier": 'ACTION_635_transfer_to_xyzf_8',
        "command": 'transfer_to_xyzf',
        "args": [7, 45, 0, RadialDirections.SOUTHEAST]
    },
    {
        "identifier": 'ACTION_635_set_priority_9',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_635_jmp_10',
        "command": 'jmp',
        "args": ['ACTION_635_visibility_on_22']
    },
    {
        "identifier": 'ACTION_635_transfer_to_xyzf_11',
        "command": 'transfer_to_xyzf',
        "args": [13, 34, 0, RadialDirections.SOUTHEAST]
    },
    {
        "identifier": 'ACTION_635_set_priority_12',
        "command": 'set_priority',
        "args": [2]
    },
    {
        "identifier": 'ACTION_635_jmp_13',
        "command": 'jmp',
        "args": ['ACTION_635_visibility_on_22']
    },
    {
        "identifier": 'ACTION_635_transfer_to_xyzf_14',
        "command": 'transfer_to_xyzf',
        "args": [14, 43, 0, RadialDirections.SOUTHEAST]
    },
    {
        "identifier": 'ACTION_635_set_priority_15',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_635_jmp_16',
        "command": 'jmp',
        "args": ['ACTION_635_visibility_on_22']
    },
    {
        "identifier": 'ACTION_635_transfer_to_xyzf_17',
        "command": 'transfer_to_xyzf',
        "args": [17, 59, 0, RadialDirections.SOUTHEAST]
    },
    {
        "identifier": 'ACTION_635_set_priority_18',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_635_jmp_19',
        "command": 'jmp',
        "args": ['ACTION_635_visibility_on_22']
    },
    {
        "identifier": 'ACTION_635_transfer_to_xyzf_20',
        "command": 'transfer_to_xyzf',
        "args": [12, 44, 0, RadialDirections.SOUTHEAST]
    },
    {
        "identifier": 'ACTION_635_set_priority_21',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_635_visibility_on_22',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_635_shadow_on_23',
        "command": 'shadow_on'
    },
    {
        "identifier": 'ACTION_635_db_24',
        "command": 'db',
        "args": [0x20, 0x04]
    },
    {
        "identifier": 'ACTION_635_db_25',
        "command": 'db',
        "args": [0x25, 0x00, 0x00, 0x68, 0xff]
    },
    {
        "identifier": 'ACTION_635_set_animation_speed_26',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_635_shift_northeast_pixels_27',
        "command": 'shift_northeast_pixels',
        "args": [4]
    },
    {
        "identifier": 'ACTION_635_set_animation_speed_28',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_635_shift_northeast_pixels_29',
        "command": 'shift_northeast_pixels',
        "args": [12]
    },
    {
        "identifier": 'ACTION_635_bpl_26_27_28_30',
        "command": 'bpl_26_27_28'
    },
    {
        "identifier": 'ACTION_635_shadow_off_31',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_635_pause_32',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_635_db_33',
        "command": 'db',
        "args": [0xfd, 0x3d, 0x1c, 0xfa, 0x71]
    },
    {
        "identifier": 'ACTION_635_play_sound_34',
        "command": 'play_sound',
        "args": [Sounds._033_JUMPING_BOUNCING_FISH, 4]
    },
    {
        "identifier": 'ACTION_635_start_loop_n_times_35',
        "command": 'start_loop_n_times',
        "args": [2]
    },
    {
        "identifier": 'ACTION_635_set_sprite_sequence_36',
        "command": 'set_sprite_sequence',
        "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_635_pause_37',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_635_set_sprite_sequence_38',
        "command": 'set_sprite_sequence',
        "args": [2, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_635_pause_39',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_635_set_sprite_sequence_40',
        "command": 'set_sprite_sequence',
        "args": [1, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_635_pause_41',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_635_end_loop_42',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_635_start_loop_n_times_43',
        "command": 'start_loop_n_times',
        "args": [1]
    },
    {
        "identifier": 'ACTION_635_visibility_off_44',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_635_pause_45',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_635_visibility_on_46',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_635_pause_47',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_635_set_sprite_sequence_48',
        "command": 'set_sprite_sequence',
        "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_635_pause_49',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_635_visibility_off_50',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_635_pause_51',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_635_visibility_on_52',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_635_pause_53',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_635_set_sprite_sequence_54',
        "command": 'set_sprite_sequence',
        "args": [2, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_635_pause_55',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_635_visibility_off_56',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_635_pause_57',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_635_visibility_on_58',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_635_pause_59',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_635_set_sprite_sequence_60',
        "command": 'set_sprite_sequence',
        "args": [1, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_635_pause_61',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_635_end_loop_62',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_635_visibility_off_63',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_635_pause_64',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_635_visibility_on_65',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_635_pause_66',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_635_set_sprite_sequence_67',
        "command": 'set_sprite_sequence',
        "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_635_pause_68',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_635_visibility_off_69',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_635_clear_solidity_bits_70',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_635_transfer_to_xyzf_71',
        "command": 'transfer_to_xyzf',
        "args": [21, 79, 0, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_635_set_sprite_sequence_72',
        "command": 'set_sprite_sequence',
        "args": [1, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_635_clear_bit_73',
        "command": 'clear_bit',
        "args": [0x7043, 3]
    },
    {
        "identifier": 'ACTION_635_clear_bit_74',
        "command": 'clear_bit',
        "args": [0x7043, 4]
    },
    {
        "identifier": 'ACTION_635_clear_bit_75',
        "command": 'clear_bit',
        "args": [0x7043, 5]
    },
    {
        "identifier": 'ACTION_635_clear_bit_76',
        "command": 'clear_bit',
        "args": [0x7043, 6]
    },
    {
        "identifier": 'ACTION_635_clear_bit_77',
        "command": 'clear_bit',
        "args": [0x7043, 7]
    },
    {
        "identifier": 'ACTION_635_clear_bit_78',
        "command": 'clear_bit',
        "args": [0x7044, 1]
    },
    {
        "identifier": 'ACTION_635_set_bit_79',
        "command": 'set_bit',
        "args": [0x7044, 5]
    },
    {
        "identifier": 'ACTION_635_ret_80',
        "command": 'ret'
    }
]
