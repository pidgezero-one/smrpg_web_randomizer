from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_299_visibility_off_0',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_299_transfer_to_xyzf_1',
        "command": 'transfer_to_xyzf',
        "args": [7, 18, 6, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_299_transfer_xyzf_pixels_2',
        "command": 'transfer_xyzf_pixels',
        "args": [4, 2, 0, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_299_set_priority_3',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_299_set_sprite_sequence_4',
        "command": 'set_sprite_sequence',
        "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_299_visibility_on_5',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_299_face_mario_6',
        "command": 'face_mario'
    },
    {
        "identifier": 'ACTION_299_jmp_if_bit_set_7',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 1, 'ACTION_299_set_random_66']
    },
    {
        "identifier": 'ACTION_299_set_bit_8',
        "command": 'set_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'ACTION_299_set_700C_to_object_coord_9',
        "command": 'set_700C_to_object_coord',
        "args": [AreaObjects.DUMMY_0X07, Coords.F]
    },
    {
        "identifier": 'ACTION_299_jmp_if_var_equals_short_10',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 0, 'ACTION_299_jmp_if_bit_set_23']
    },
    {
        "identifier": 'ACTION_299_jmp_if_var_equals_short_11',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 1, 'ACTION_299_jmp_if_bit_set_23']
    },
    {
        "identifier": 'ACTION_299_jmp_if_var_equals_short_12',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 2, 'ACTION_299_jmp_if_bit_set_35']
    },
    {
        "identifier": 'ACTION_299_jmp_if_var_equals_short_13',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 4, 'ACTION_299_jmp_if_bit_set_29']
    },
    {
        "identifier": 'ACTION_299_jmp_if_var_equals_short_14',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 5, 'ACTION_299_jmp_if_bit_set_41']
    },
    {
        "identifier": 'ACTION_299_jmp_if_var_equals_short_15',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 6, 'ACTION_299_jmp_if_bit_set_41']
    },
    {
        "identifier": 'ACTION_299_jmp_if_var_equals_short_16',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 7, 'ACTION_299_jmp_if_bit_set_23']
    },
    {
        "identifier": 'ACTION_299_jmp_if_bit_set_17',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 1, 'ACTION_299_clear_bit_47']
    },
    {
        "identifier": 'ACTION_299_set_bit_18',
        "command": 'set_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'ACTION_299_set_animation_speed_19',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_299_jump_to_height_silent_20',
        "command": 'jump_to_height_silent',
        "args": [64]
    },
    {
        "identifier": 'ACTION_299_shift_southwest_pixels_21',
        "command": 'shift_southwest_pixels',
        "args": [48]
    },
    {
        "identifier": 'ACTION_299_jmp_22',
        "command": 'jmp',
        "args": ['ACTION_299_set_priority_62']
    },
    {
        "identifier": 'ACTION_299_jmp_if_bit_set_23',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 2, 'ACTION_299_clear_bit_50']
    },
    {
        "identifier": 'ACTION_299_set_bit_24',
        "command": 'set_bit',
        "args": [0x7043, 2]
    },
    {
        "identifier": 'ACTION_299_set_animation_speed_25',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_299_jump_to_height_silent_26',
        "command": 'jump_to_height_silent',
        "args": [64]
    },
    {
        "identifier": 'ACTION_299_shift_southeast_pixels_27',
        "command": 'shift_southeast_pixels',
        "args": [48]
    },
    {
        "identifier": 'ACTION_299_jmp_28',
        "command": 'jmp',
        "args": ['ACTION_299_set_priority_62']
    },
    {
        "identifier": 'ACTION_299_jmp_if_bit_set_29',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 3, 'ACTION_299_clear_bit_53']
    },
    {
        "identifier": 'ACTION_299_set_bit_30',
        "command": 'set_bit',
        "args": [0x7043, 3]
    },
    {
        "identifier": 'ACTION_299_set_animation_speed_31',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FASTER, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_299_jump_to_height_silent_32',
        "command": 'jump_to_height_silent',
        "args": [64]
    },
    {
        "identifier": 'ACTION_299_shift_west_pixels_33',
        "command": 'shift_west_pixels',
        "args": [72]
    },
    {
        "identifier": 'ACTION_299_jmp_34',
        "command": 'jmp',
        "args": ['ACTION_299_set_priority_62']
    },
    {
        "identifier": 'ACTION_299_jmp_if_bit_set_35',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 4, 'ACTION_299_clear_bit_56']
    },
    {
        "identifier": 'ACTION_299_set_bit_36',
        "command": 'set_bit',
        "args": [0x7043, 4]
    },
    {
        "identifier": 'ACTION_299_jump_to_height_silent_37',
        "command": 'jump_to_height_silent',
        "args": [80]
    },
    {
        "identifier": 'ACTION_299_set_animation_speed_38',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_299_shift_south_pixels_39',
        "command": 'shift_south_pixels',
        "args": [36]
    },
    {
        "identifier": 'ACTION_299_jmp_40',
        "command": 'jmp',
        "args": ['ACTION_299_set_priority_62']
    },
    {
        "identifier": 'ACTION_299_jmp_if_bit_set_41',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 5, 'ACTION_299_clear_bit_59']
    },
    {
        "identifier": 'ACTION_299_set_bit_42',
        "command": 'set_bit',
        "args": [0x7043, 5]
    },
    {
        "identifier": 'ACTION_299_set_animation_speed_43',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_299_jump_to_height_silent_44',
        "command": 'jump_to_height_silent',
        "args": [64]
    },
    {
        "identifier": 'ACTION_299_shift_northwest_pixels_45',
        "command": 'shift_northwest_pixels',
        "args": [48]
    },
    {
        "identifier": 'ACTION_299_jmp_46',
        "command": 'jmp',
        "args": ['ACTION_299_set_priority_62']
    },
    {
        "identifier": 'ACTION_299_clear_bit_47',
        "command": 'clear_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'ACTION_299_jmp_if_random_above_128_48',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_299_jmp_if_bit_set_35']
    },
    {
        "identifier": 'ACTION_299_jmp_49',
        "command": 'jmp',
        "args": ['ACTION_299_jmp_if_bit_set_29']
    },
    {
        "identifier": 'ACTION_299_clear_bit_50',
        "command": 'clear_bit',
        "args": [0x7043, 2]
    },
    {
        "identifier": 'ACTION_299_jmp_if_random_above_128_51',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_299_jmp_if_bit_set_17']
    },
    {
        "identifier": 'ACTION_299_jmp_52',
        "command": 'jmp',
        "args": ['ACTION_299_jmp_if_bit_set_35']
    },
    {
        "identifier": 'ACTION_299_clear_bit_53',
        "command": 'clear_bit',
        "args": [0x7043, 3]
    },
    {
        "identifier": 'ACTION_299_jmp_if_random_above_128_54',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_299_jmp_if_bit_set_41']
    },
    {
        "identifier": 'ACTION_299_jmp_55',
        "command": 'jmp',
        "args": ['ACTION_299_jmp_if_bit_set_17']
    },
    {
        "identifier": 'ACTION_299_clear_bit_56',
        "command": 'clear_bit',
        "args": [0x7043, 4]
    },
    {
        "identifier": 'ACTION_299_jmp_if_random_above_128_57',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_299_jmp_if_bit_set_17']
    },
    {
        "identifier": 'ACTION_299_jmp_58',
        "command": 'jmp',
        "args": ['ACTION_299_jmp_if_bit_set_23']
    },
    {
        "identifier": 'ACTION_299_clear_bit_59',
        "command": 'clear_bit',
        "args": [0x7043, 5]
    },
    {
        "identifier": 'ACTION_299_jmp_if_random_above_128_60',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_299_jmp_if_bit_set_29']
    },
    {
        "identifier": 'ACTION_299_jmp_61',
        "command": 'jmp',
        "args": ['ACTION_299_jmp_if_bit_set_17']
    },
    {
        "identifier": 'ACTION_299_set_priority_62',
        "command": 'set_priority',
        "args": [2]
    },
    {
        "identifier": 'ACTION_299_pause_63',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_299_db_64',
        "command": 'db',
        "args": [0xfd, 0x3d, 0x07, 0x6e, 0x37]
    },
    {
        "identifier": 'ACTION_299_jmp_65',
        "command": 'jmp',
        "args": ['ACTION_302_pause_0']
    },
    {
        "identifier": 'ACTION_299_set_random_66',
        "command": 'set_random',
        "args": [0x700c, 8]
    },
    {
        "identifier": 'ACTION_299_jmp_67',
        "command": 'jmp',
        "args": ['ACTION_299_jmp_if_var_equals_short_10']
    }
]
