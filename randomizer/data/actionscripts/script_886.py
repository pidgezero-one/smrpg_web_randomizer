from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_886_clear_bit_0',
        "command": 'clear_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'ACTION_886_set_700C_to_current_level_1',
        "command": 'set_700C_to_current_level'
    },
    {
        "identifier": 'ACTION_886_jmp_if_700C_equals_short_2',
        "command": 'jmp_if_700C_equals_short',
        "args": [410, 'ACTION_886_clear_bit_34']
    },
    {
        "identifier": 'ACTION_886_set_sprite_sequence_3',
        "command": 'set_sprite_sequence',
        "args": [4, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_886_jmp_if_random_above_128_4',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_886_pause_6']
    },
    {
        "identifier": 'ACTION_886_pause_5',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_886_pause_6',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'ACTION_886_set_sprite_sequence_7',
        "command": 'set_sprite_sequence',
        "args": [5, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_886_pause_8',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_886_set_sprite_sequence_9',
        "command": 'set_sprite_sequence',
        "args": [6, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_886_pause_10',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_886_set_sprite_sequence_11',
        "command": 'set_sprite_sequence',
        "args": [7, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_886_pause_12',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_886_set_sprite_sequence_13',
        "command": 'set_sprite_sequence',
        "args": [8, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_886_pause_14',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_886_set_sprite_sequence_15',
        "command": 'set_sprite_sequence',
        "args": [9, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_886_pause_16',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_886_set_sprite_sequence_17',
        "command": 'set_sprite_sequence',
        "args": [10, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_886_pause_18',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_886_set_sprite_sequence_19',
        "command": 'set_sprite_sequence',
        "args": [11, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_886_pause_20',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_886_set_sprite_sequence_21',
        "command": 'set_sprite_sequence',
        "args": [12, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_886_pause_22',
        "command": 'pause',
        "args": [6]
    },
    {
        "identifier": 'ACTION_886_set_sprite_sequence_23',
        "command": 'set_sprite_sequence',
        "args": [13, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_886_pause_24',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_886_set_bit_25',
        "command": 'set_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'ACTION_886_pause_26',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_886_jmp_if_random_above_128_27',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_886_set_sprite_sequence_29']
    },
    {
        "identifier": 'ACTION_886_pause_28',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'ACTION_886_set_sprite_sequence_29',
        "command": 'set_sprite_sequence',
        "args": [14, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_886_pause_30',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_886_jmp_if_random_above_128_31',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_886_clear_bit_0']
    },
    {
        "identifier": 'ACTION_886_pause_32',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'ACTION_886_jmp_33',
        "command": 'jmp',
        "args": ['ACTION_886_clear_bit_0']
    },
    {
        "identifier": 'ACTION_886_clear_bit_34',
        "command": 'clear_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'ACTION_886_set_sprite_sequence_35',
        "command": 'set_sprite_sequence',
        "args": [4, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_886_jmp_if_random_above_128_36',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_886_pause_38']
    },
    {
        "identifier": 'ACTION_886_pause_37',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_886_pause_38',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'ACTION_886_set_sprite_sequence_39',
        "command": 'set_sprite_sequence',
        "args": [5, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_886_pause_40',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_886_set_sprite_sequence_41',
        "command": 'set_sprite_sequence',
        "args": [6, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_886_pause_42',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_886_set_sprite_sequence_43',
        "command": 'set_sprite_sequence',
        "args": [7, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_886_pause_44',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_886_set_sprite_sequence_45',
        "command": 'set_sprite_sequence',
        "args": [8, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_886_pause_46',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_886_set_sprite_sequence_47',
        "command": 'set_sprite_sequence',
        "args": [9, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_886_pause_48',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_886_set_sprite_sequence_49',
        "command": 'set_sprite_sequence',
        "args": [10, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_886_pause_50',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_886_set_sprite_sequence_51',
        "command": 'set_sprite_sequence',
        "args": [11, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_886_pause_52',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_886_set_sprite_sequence_53',
        "command": 'set_sprite_sequence',
        "args": [12, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_886_pause_54',
        "command": 'pause',
        "args": [6]
    },
    {
        "identifier": 'ACTION_886_set_sprite_sequence_55',
        "command": 'set_sprite_sequence',
        "args": [13, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_886_pause_56',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_886_set_bit_57',
        "command": 'set_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'ACTION_886_pause_58',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_886_jmp_if_random_above_128_59',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_886_set_sprite_sequence_61']
    },
    {
        "identifier": 'ACTION_886_pause_60',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'ACTION_886_set_sprite_sequence_61',
        "command": 'set_sprite_sequence',
        "args": [14, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_886_pause_62',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_886_pause_63',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'ACTION_886_jmp_if_random_above_128_64',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_886_clear_bit_34']
    },
    {
        "identifier": 'ACTION_886_pause_65',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_886_jmp_66',
        "command": 'jmp',
        "args": ['ACTION_886_clear_bit_34']
    }
]
