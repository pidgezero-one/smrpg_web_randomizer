from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_488_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7083, 6, 'ACTION_488_clear_bit_10']
    },
    {
        "identifier": 'ACTION_488_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7045, 5, 'ACTION_488_clear_bit_10']
    },
    {
        "identifier": 'ACTION_488_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x7045, 7, 'ACTION_488_clear_bit_10']
    },
    {
        "identifier": 'ACTION_488_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x7046, 0, 'ACTION_488_clear_bit_10']
    },
    {
        "identifier": 'ACTION_488_jmp_if_bit_set_4',
        "command": 'jmp_if_bit_set',
        "args": [0x7045, 0, 'ACTION_488_shirt_to_xy_coords_24']
    },
    {
        "identifier": 'ACTION_488_jmp_if_bit_set_5',
        "command": 'jmp_if_bit_set',
        "args": [0x7045, 1, 'ACTION_488_shirt_to_xy_coords_36']
    },
    {
        "identifier": 'ACTION_488_jmp_if_bit_set_6',
        "command": 'jmp_if_bit_set',
        "args": [0x7045, 2, 'ACTION_488_clear_bit_10']
    },
    {
        "identifier": 'ACTION_488_jmp_if_bit_set_7',
        "command": 'jmp_if_bit_set',
        "args": [0x7045, 3, 'ACTION_488_shirt_to_xy_coords_48']
    },
    {
        "identifier": 'ACTION_488_jmp_if_bit_set_8',
        "command": 'jmp_if_bit_set',
        "args": [0x7045, 4, 'ACTION_488_shirt_to_xy_coords_60']
    },
    {
        "identifier": 'ACTION_488_jmp_if_bit_set_9',
        "command": 'jmp_if_bit_set',
        "args": [0x7046, 1, 'ACTION_488_shirt_to_xy_coords_13']
    },
    {
        "identifier": 'ACTION_488_clear_bit_10',
        "command": 'clear_bit',
        "args": [0x7045, 5]
    },
    {
        "identifier": 'ACTION_488_visibility_off_11',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_488_ret_12',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_488_shirt_to_xy_coords_13',
        "command": 'shirt_to_xy_coords',
        "args": [8, 61]
    },
    {
        "identifier": 'ACTION_488_set_sprite_sequence_14',
        "command": 'set_sprite_sequence',
        "args": [8, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_488_pause_15',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_488_db_16',
        "command": 'db',
        "args": [0x3b, 0x00, 0x00, 0x05, 0xe4, 0x5d]
    },
    {
        "identifier": 'ACTION_488_jmp_17',
        "command": 'jmp',
        "args": ['ACTION_488_pause_15']
    },
    {
        "identifier": 'ACTION_488_set_animation_speed_18',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_488_set_sprite_sequence_19',
        "command": 'set_sprite_sequence',
        "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_488_shift_southeast_steps_20',
        "command": 'shift_southeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_488_shift_southeast_pixels_21',
        "command": 'shift_southeast_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_488_visibility_off_22',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_488_ret_23',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_488_shirt_to_xy_coords_24',
        "command": 'shirt_to_xy_coords',
        "args": [8, 47]
    },
    {
        "identifier": 'ACTION_488_shift_southeast_pixels_25',
        "command": 'shift_southeast_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_488_set_sprite_sequence_26',
        "command": 'set_sprite_sequence',
        "args": [9, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_488_pause_27',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_488_db_28',
        "command": 'db',
        "args": [0x3b, 0x00, 0x00, 0x05, 0x02, 0x5e]
    },
    {
        "identifier": 'ACTION_488_jmp_29',
        "command": 'jmp',
        "args": ['ACTION_488_pause_27']
    },
    {
        "identifier": 'ACTION_488_set_animation_speed_30',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_488_set_sprite_sequence_31',
        "command": 'set_sprite_sequence',
        "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_488_shift_northeast_steps_32',
        "command": 'shift_northeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_488_shift_northeast_pixels_33',
        "command": 'shift_northeast_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_488_visibility_off_34',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_488_ret_35',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_488_shirt_to_xy_coords_36',
        "command": 'shirt_to_xy_coords',
        "args": [8, 47]
    },
    {
        "identifier": 'ACTION_488_shift_southeast_pixels_37',
        "command": 'shift_southeast_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_488_set_sprite_sequence_38',
        "command": 'set_sprite_sequence',
        "args": [6, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_488_pause_39',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_488_db_40',
        "command": 'db',
        "args": [0x3b, 0x00, 0x00, 0x05, 0x20, 0x5e]
    },
    {
        "identifier": 'ACTION_488_jmp_41',
        "command": 'jmp',
        "args": ['ACTION_488_pause_39']
    },
    {
        "identifier": 'ACTION_488_set_animation_speed_42',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_488_set_sprite_sequence_43',
        "command": 'set_sprite_sequence',
        "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_488_shift_northeast_steps_44',
        "command": 'shift_northeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_488_shift_northeast_pixels_45',
        "command": 'shift_northeast_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_488_visibility_off_46',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_488_ret_47',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_488_shirt_to_xy_coords_48',
        "command": 'shirt_to_xy_coords',
        "args": [8, 47]
    },
    {
        "identifier": 'ACTION_488_shift_southeast_pixels_49',
        "command": 'shift_southeast_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_488_set_sprite_sequence_50',
        "command": 'set_sprite_sequence',
        "args": [9, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_488_pause_51',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_488_db_52',
        "command": 'db',
        "args": [0x3b, 0x00, 0x00, 0x05, 0x3e, 0x5e]
    },
    {
        "identifier": 'ACTION_488_jmp_53',
        "command": 'jmp',
        "args": ['ACTION_488_pause_51']
    },
    {
        "identifier": 'ACTION_488_set_animation_speed_54',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_488_set_sprite_sequence_55',
        "command": 'set_sprite_sequence',
        "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_488_shift_northeast_steps_56',
        "command": 'shift_northeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_488_shift_northeast_pixels_57',
        "command": 'shift_northeast_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_488_visibility_off_58',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_488_ret_59',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_488_shirt_to_xy_coords_60',
        "command": 'shirt_to_xy_coords',
        "args": [3, 47]
    },
    {
        "identifier": 'ACTION_488_set_animation_speed_61',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_488_set_sprite_sequence_62',
        "command": 'set_sprite_sequence',
        "args": [6, 1, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_488_pause_63',
        "command": 'pause',
        "args": [52]
    },
    {
        "identifier": 'ACTION_488_set_animation_speed_64',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_488_set_sprite_sequence_65',
        "command": 'set_sprite_sequence',
        "args": [3, 1, [_0x08Flags.LOOPING_OFF, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_488_pause_66',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'ACTION_488_set_animation_speed_67',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_488_set_sprite_sequence_68',
        "command": 'set_sprite_sequence',
        "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_488_shift_northwest_steps_69',
        "command": 'shift_northwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_488_visibility_off_70',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_488_ret_71',
        "command": 'ret'
    }
]
