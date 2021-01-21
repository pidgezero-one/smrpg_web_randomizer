from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_783_set_bit_0',
        "command": 'set_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'ACTION_783_set_bit_1',
        "command": 'set_bit',
        "args": [0x7044, 6]
    },
    {
        "identifier": 'ACTION_783_set_sprite_sequence_2',
        "command": 'set_sprite_sequence',
        "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_783_jmp_if_bit_clear_3',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 0, 'ACTION_783_clear_bit_61']
    },
    {
        "identifier": 'ACTION_783_set_short_4',
        "command": 'set_short',
        "args": [0x7032, 0x0000]
    },
    {
        "identifier": 'ACTION_783_set_short_5',
        "command": 'set_short',
        "args": [0x7024, 0x0500]
    },
    {
        "identifier": 'ACTION_783_pause_6',
        "command": 'pause',
        "args": [6]
    },
    {
        "identifier": 'ACTION_783_set_short_7',
        "command": 'set_short',
        "args": [0x7024, 0x0501]
    },
    {
        "identifier": 'ACTION_783_pause_8',
        "command": 'pause',
        "args": [6]
    },
    {
        "identifier": 'ACTION_783_jmp_if_bit_clear_9',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 0, 'ACTION_783_clear_bit_61']
    },
    {
        "identifier": 'ACTION_783_set_short_10',
        "command": 'set_short',
        "args": [0x7024, 0x0502]
    },
    {
        "identifier": 'ACTION_783_pause_11',
        "command": 'pause',
        "args": [6]
    },
    {
        "identifier": 'ACTION_783_set_short_12',
        "command": 'set_short',
        "args": [0x7024, 0x0503]
    },
    {
        "identifier": 'ACTION_783_pause_13',
        "command": 'pause',
        "args": [6]
    },
    {
        "identifier": 'ACTION_783_jmp_if_bit_clear_14',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 0, 'ACTION_783_clear_bit_61']
    },
    {
        "identifier": 'ACTION_783_jmp_if_bit_clear_15',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 4, 'ACTION_783_set_sprite_sequence_20']
    },
    {
        "identifier": 'ACTION_783_jmp_if_bit_set_16',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 2, 'ACTION_783_play_sound_19']
    },
    {
        "identifier": 'ACTION_783_play_sound_17',
        "command": 'play_sound',
        "args": [Sounds._144_CLICK, 4]
    },
    {
        "identifier": 'ACTION_783_jmp_18',
        "command": 'jmp',
        "args": ['ACTION_783_set_sprite_sequence_20']
    },
    {
        "identifier": 'ACTION_783_play_sound_19',
        "command": 'play_sound',
        "args": [Sounds._143_METRONOME_UPBEAT_DING, 4]
    },
    {
        "identifier": 'ACTION_783_set_sprite_sequence_20',
        "command": 'set_sprite_sequence',
        "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_783_set_short_21',
        "command": 'set_short',
        "args": [0x7032, 0x0005]
    },
    {
        "identifier": 'ACTION_783_pause_22',
        "command": 'pause',
        "args": [6]
    },
    {
        "identifier": 'ACTION_783_set_short_23',
        "command": 'set_short',
        "args": [0x7024, 0x0502]
    },
    {
        "identifier": 'ACTION_783_pause_24',
        "command": 'pause',
        "args": [6]
    },
    {
        "identifier": 'ACTION_783_set_short_25',
        "command": 'set_short',
        "args": [0x7024, 0x0501]
    },
    {
        "identifier": 'ACTION_783_pause_26',
        "command": 'pause',
        "args": [6]
    },
    {
        "identifier": 'ACTION_783_set_short_27',
        "command": 'set_short',
        "args": [0x7024, 0x0500]
    },
    {
        "identifier": 'ACTION_783_pause_28',
        "command": 'pause',
        "args": [6]
    },
    {
        "identifier": 'ACTION_783_jmp_if_bit_clear_29',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 4, 'ACTION_783_set_sprite_sequence_31']
    },
    {
        "identifier": 'ACTION_783_play_sound_30',
        "command": 'play_sound',
        "args": [Sounds._144_CLICK, 4]
    },
    {
        "identifier": 'ACTION_783_set_sprite_sequence_31',
        "command": 'set_sprite_sequence',
        "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_783_jmp_if_bit_clear_32',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 0, 'ACTION_783_clear_bit_61']
    },
    {
        "identifier": 'ACTION_783_set_short_33',
        "command": 'set_short',
        "args": [0x7032, 0x0000]
    },
    {
        "identifier": 'ACTION_783_set_short_34',
        "command": 'set_short',
        "args": [0x7024, 0x0100]
    },
    {
        "identifier": 'ACTION_783_pause_35',
        "command": 'pause',
        "args": [6]
    },
    {
        "identifier": 'ACTION_783_set_short_36',
        "command": 'set_short',
        "args": [0x7024, 0x0101]
    },
    {
        "identifier": 'ACTION_783_pause_37',
        "command": 'pause',
        "args": [6]
    },
    {
        "identifier": 'ACTION_783_jmp_if_bit_clear_38',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 0, 'ACTION_783_clear_bit_61']
    },
    {
        "identifier": 'ACTION_783_set_short_39',
        "command": 'set_short',
        "args": [0x7024, 0x0102]
    },
    {
        "identifier": 'ACTION_783_pause_40',
        "command": 'pause',
        "args": [6]
    },
    {
        "identifier": 'ACTION_783_set_short_41',
        "command": 'set_short',
        "args": [0x7024, 0x0103]
    },
    {
        "identifier": 'ACTION_783_pause_42',
        "command": 'pause',
        "args": [6]
    },
    {
        "identifier": 'ACTION_783_jmp_if_bit_clear_43',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 0, 'ACTION_783_clear_bit_61']
    },
    {
        "identifier": 'ACTION_783_jmp_if_bit_clear_44',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 4, 'ACTION_783_set_sprite_sequence_49']
    },
    {
        "identifier": 'ACTION_783_jmp_if_bit_set_45',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 2, 'ACTION_783_play_sound_48']
    },
    {
        "identifier": 'ACTION_783_play_sound_46',
        "command": 'play_sound',
        "args": [Sounds._143_METRONOME_UPBEAT_DING, 4]
    },
    {
        "identifier": 'ACTION_783_jmp_47',
        "command": 'jmp',
        "args": ['ACTION_783_set_sprite_sequence_49']
    },
    {
        "identifier": 'ACTION_783_play_sound_48',
        "command": 'play_sound',
        "args": [Sounds._144_CLICK, 4]
    },
    {
        "identifier": 'ACTION_783_set_sprite_sequence_49',
        "command": 'set_sprite_sequence',
        "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_783_set_short_50',
        "command": 'set_short',
        "args": [0x7032, 0x0001]
    },
    {
        "identifier": 'ACTION_783_pause_51',
        "command": 'pause',
        "args": [6]
    },
    {
        "identifier": 'ACTION_783_set_short_52',
        "command": 'set_short',
        "args": [0x7024, 0x0102]
    },
    {
        "identifier": 'ACTION_783_pause_53',
        "command": 'pause',
        "args": [6]
    },
    {
        "identifier": 'ACTION_783_set_short_54',
        "command": 'set_short',
        "args": [0x7024, 0x0101]
    },
    {
        "identifier": 'ACTION_783_pause_55',
        "command": 'pause',
        "args": [6]
    },
    {
        "identifier": 'ACTION_783_set_short_56',
        "command": 'set_short',
        "args": [0x7024, 0x0100]
    },
    {
        "identifier": 'ACTION_783_pause_57',
        "command": 'pause',
        "args": [6]
    },
    {
        "identifier": 'ACTION_783_jmp_if_bit_clear_58',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 4, 'ACTION_783_set_sprite_sequence_2']
    },
    {
        "identifier": 'ACTION_783_play_sound_59',
        "command": 'play_sound',
        "args": [Sounds._144_CLICK, 4]
    },
    {
        "identifier": 'ACTION_783_jmp_60',
        "command": 'jmp',
        "args": ['ACTION_783_set_sprite_sequence_2']
    },
    {
        "identifier": 'ACTION_783_clear_bit_61',
        "command": 'clear_bit',
        "args": [0x7044, 6]
    },
    {
        "identifier": 'ACTION_783_reset_properties_62',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_783_ret_63',
        "command": 'ret'
    }
]
