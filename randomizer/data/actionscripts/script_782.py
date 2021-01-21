from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_782_set_bit_0',
        "command": 'set_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'ACTION_782_set_bit_1',
        "command": 'set_bit',
        "args": [0x7044, 6]
    },
    {
        "identifier": 'ACTION_782_set_sprite_sequence_2',
        "command": 'set_sprite_sequence',
        "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_782_jmp_if_bit_clear_3',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 0, 'ACTION_783_clear_bit_61']
    },
    {
        "identifier": 'ACTION_782_set_short_4',
        "command": 'set_short',
        "args": [0x7032, 0x0000]
    },
    {
        "identifier": 'ACTION_782_set_short_5',
        "command": 'set_short',
        "args": [0x7024, 0x0700]
    },
    {
        "identifier": 'ACTION_782_pause_6',
        "command": 'pause',
        "args": [6]
    },
    {
        "identifier": 'ACTION_782_set_short_7',
        "command": 'set_short',
        "args": [0x7024, 0x0701]
    },
    {
        "identifier": 'ACTION_782_pause_8',
        "command": 'pause',
        "args": [6]
    },
    {
        "identifier": 'ACTION_782_jmp_if_bit_clear_9',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 0, 'ACTION_783_clear_bit_61']
    },
    {
        "identifier": 'ACTION_782_set_short_10',
        "command": 'set_short',
        "args": [0x7024, 0x0702]
    },
    {
        "identifier": 'ACTION_782_pause_11',
        "command": 'pause',
        "args": [6]
    },
    {
        "identifier": 'ACTION_782_set_short_12',
        "command": 'set_short',
        "args": [0x7024, 0x0703]
    },
    {
        "identifier": 'ACTION_782_pause_13',
        "command": 'pause',
        "args": [6]
    },
    {
        "identifier": 'ACTION_782_jmp_if_bit_clear_14',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 0, 'ACTION_782_clear_bit_55']
    },
    {
        "identifier": 'ACTION_782_jmp_if_bit_clear_15',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 4, 'ACTION_782_set_sprite_sequence_17']
    },
    {
        "identifier": 'ACTION_782_play_sound_16',
        "command": 'play_sound',
        "args": [Sounds._143_METRONOME_UPBEAT_DING, 4]
    },
    {
        "identifier": 'ACTION_782_set_sprite_sequence_17',
        "command": 'set_sprite_sequence',
        "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_782_set_short_18',
        "command": 'set_short',
        "args": [0x7032, 0x0007]
    },
    {
        "identifier": 'ACTION_782_pause_19',
        "command": 'pause',
        "args": [6]
    },
    {
        "identifier": 'ACTION_782_set_short_20',
        "command": 'set_short',
        "args": [0x7024, 0x0702]
    },
    {
        "identifier": 'ACTION_782_pause_21',
        "command": 'pause',
        "args": [6]
    },
    {
        "identifier": 'ACTION_782_set_short_22',
        "command": 'set_short',
        "args": [0x7024, 0x0701]
    },
    {
        "identifier": 'ACTION_782_pause_23',
        "command": 'pause',
        "args": [6]
    },
    {
        "identifier": 'ACTION_782_set_short_24',
        "command": 'set_short',
        "args": [0x7024, 0x0700]
    },
    {
        "identifier": 'ACTION_782_pause_25',
        "command": 'pause',
        "args": [6]
    },
    {
        "identifier": 'ACTION_782_jmp_if_bit_clear_26',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 4, 'ACTION_782_set_sprite_sequence_28']
    },
    {
        "identifier": 'ACTION_782_play_sound_27',
        "command": 'play_sound',
        "args": [Sounds._144_CLICK, 4]
    },
    {
        "identifier": 'ACTION_782_set_sprite_sequence_28',
        "command": 'set_sprite_sequence',
        "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_782_jmp_if_bit_clear_29',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 0, 'ACTION_783_clear_bit_61']
    },
    {
        "identifier": 'ACTION_782_set_short_30',
        "command": 'set_short',
        "args": [0x7032, 0x0000]
    },
    {
        "identifier": 'ACTION_782_set_short_31',
        "command": 'set_short',
        "args": [0x7024, 0x0300]
    },
    {
        "identifier": 'ACTION_782_pause_32',
        "command": 'pause',
        "args": [6]
    },
    {
        "identifier": 'ACTION_782_set_short_33',
        "command": 'set_short',
        "args": [0x7024, 0x0301]
    },
    {
        "identifier": 'ACTION_782_pause_34',
        "command": 'pause',
        "args": [6]
    },
    {
        "identifier": 'ACTION_782_jmp_if_bit_clear_35',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 0, 'ACTION_783_clear_bit_61']
    },
    {
        "identifier": 'ACTION_782_set_short_36',
        "command": 'set_short',
        "args": [0x7024, 0x0302]
    },
    {
        "identifier": 'ACTION_782_pause_37',
        "command": 'pause',
        "args": [6]
    },
    {
        "identifier": 'ACTION_782_set_short_38',
        "command": 'set_short',
        "args": [0x7024, 0x0303]
    },
    {
        "identifier": 'ACTION_782_pause_39',
        "command": 'pause',
        "args": [6]
    },
    {
        "identifier": 'ACTION_782_jmp_if_bit_clear_40',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 0, 'ACTION_782_clear_bit_55']
    },
    {
        "identifier": 'ACTION_782_jmp_if_bit_clear_41',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 4, 'ACTION_782_set_sprite_sequence_43']
    },
    {
        "identifier": 'ACTION_782_play_sound_42',
        "command": 'play_sound',
        "args": [Sounds._144_CLICK, 4]
    },
    {
        "identifier": 'ACTION_782_set_sprite_sequence_43',
        "command": 'set_sprite_sequence',
        "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_782_set_short_44',
        "command": 'set_short',
        "args": [0x7032, 0x0003]
    },
    {
        "identifier": 'ACTION_782_pause_45',
        "command": 'pause',
        "args": [6]
    },
    {
        "identifier": 'ACTION_782_set_short_46',
        "command": 'set_short',
        "args": [0x7024, 0x0302]
    },
    {
        "identifier": 'ACTION_782_pause_47',
        "command": 'pause',
        "args": [6]
    },
    {
        "identifier": 'ACTION_782_set_short_48',
        "command": 'set_short',
        "args": [0x7024, 0x0301]
    },
    {
        "identifier": 'ACTION_782_pause_49',
        "command": 'pause',
        "args": [6]
    },
    {
        "identifier": 'ACTION_782_set_short_50',
        "command": 'set_short',
        "args": [0x7024, 0x0300]
    },
    {
        "identifier": 'ACTION_782_pause_51',
        "command": 'pause',
        "args": [6]
    },
    {
        "identifier": 'ACTION_782_jmp_if_bit_clear_52',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 4, 'ACTION_782_set_sprite_sequence_2']
    },
    {
        "identifier": 'ACTION_782_play_sound_53',
        "command": 'play_sound',
        "args": [Sounds._144_CLICK, 4]
    },
    {
        "identifier": 'ACTION_782_jmp_54',
        "command": 'jmp',
        "args": ['ACTION_782_set_sprite_sequence_2']
    },
    {
        "identifier": 'ACTION_782_clear_bit_55',
        "command": 'clear_bit',
        "args": [0x7044, 6]
    },
    {
        "identifier": 'ACTION_782_reset_properties_56',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_782_ret_57',
        "command": 'ret'
    }
]
