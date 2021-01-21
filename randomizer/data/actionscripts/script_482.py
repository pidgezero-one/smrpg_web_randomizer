from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_482_clear_bit_0',
        "command": 'clear_bit',
        "args": [0x7047, 0]
    },
    {
        "identifier": 'ACTION_482_pause_1',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'ACTION_482_overwrite_solidity_2',
        "command": 'overwrite_solidity',
        "args": [[]]
    },
    {
        "identifier": 'ACTION_482_set_priority_3',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_482_shadow_off_4',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_482_face_south_5',
        "command": 'face_south'
    },
    {
        "identifier": 'ACTION_482_jmp_if_bit_set_6',
        "command": 'jmp_if_bit_set',
        "args": [0x7047, 4, 'ACTION_482_clear_bit_18']
    },
    {
        "identifier": 'ACTION_482_set_sprite_sequence_7',
        "command": 'set_sprite_sequence',
        "args": [0, inc_sprite=1, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_482_visibility_on_8',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_482_db_9',
        "command": 'db',
        "args": [0x20, 0x07]
    },
    {
        "identifier": 'ACTION_482_db_10',
        "command": 'db',
        "args": [0x24, 0x00, 0x00, 0xb0, 0x00]
    },
    {
        "identifier": 'ACTION_482_db_11',
        "command": 'db',
        "args": [0x25, 0x80, 0x09, 0x80, 0xff]
    },
    {
        "identifier": 'ACTION_482_pause_12',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'ACTION_482_shadow_on_13',
        "command": 'shadow_on'
    },
    {
        "identifier": 'ACTION_482_pause_14',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'ACTION_482_bpl_26_27_28_15',
        "command": 'bpl_26_27_28'
    },
    {
        "identifier": 'ACTION_482_db_16',
        "command": 'db',
        "args": [0xfd, 0x9c, 0x3a]
    },
    {
        "identifier": 'ACTION_482_ret_17',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_482_clear_bit_18',
        "command": 'clear_bit',
        "args": [0x7047, 4]
    },
    {
        "identifier": 'ACTION_482_face_southwest_19',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_482_set_sprite_sequence_20',
        "command": 'set_sprite_sequence',
        "args": [0, inc_sprite=3, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_482_visibility_on_21',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_482_db_22',
        "command": 'db',
        "args": [0x20, 0x07]
    },
    {
        "identifier": 'ACTION_482_db_23',
        "command": 'db',
        "args": [0x24, 0x00, 0x00, 0xb0, 0x00]
    },
    {
        "identifier": 'ACTION_482_db_24',
        "command": 'db',
        "args": [0x25, 0x80, 0x09, 0x80, 0xff]
    },
    {
        "identifier": 'ACTION_482_pause_25',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'ACTION_482_shadow_on_26',
        "command": 'shadow_on'
    },
    {
        "identifier": 'ACTION_482_pause_27',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'ACTION_482_play_sound_28',
        "command": 'play_sound',
        "args": [Sounds._022_CLOSE_DOOR, 4]
    },
    {
        "identifier": 'ACTION_482_db_29',
        "command": 'db',
        "args": [0x24, 0x00, 0x00, 0x00, 0x00]
    },
    {
        "identifier": 'ACTION_482_db_30',
        "command": 'db',
        "args": [0x25, 0xc0, 0x06, 0x80, 0xff]
    },
    {
        "identifier": 'ACTION_482_play_sound_31',
        "command": 'play_sound',
        "args": [Sounds._022_CLOSE_DOOR, 4]
    },
    {
        "identifier": 'ACTION_482_pause_32',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_482_play_sound_33',
        "command": 'play_sound',
        "args": [Sounds._022_CLOSE_DOOR, 4]
    },
    {
        "identifier": 'ACTION_482_db_34',
        "command": 'db',
        "args": [0x25, 0x80, 0x04, 0x80, 0xff]
    },
    {
        "identifier": 'ACTION_482_pause_35',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'ACTION_482_play_sound_36',
        "command": 'play_sound',
        "args": [Sounds._022_CLOSE_DOOR, 4]
    },
    {
        "identifier": 'ACTION_482_db_37',
        "command": 'db',
        "args": [0x25, 0x40, 0x02, 0x80, 0xff]
    },
    {
        "identifier": 'ACTION_482_pause_38',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'ACTION_482_play_sound_39',
        "command": 'play_sound',
        "args": [Sounds._022_CLOSE_DOOR, 4]
    },
    {
        "identifier": 'ACTION_482_bpl_26_27_28_40',
        "command": 'bpl_26_27_28'
    },
    {
        "identifier": 'ACTION_482_pause_41',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'ACTION_482_jmp_42',
        "command": 'jmp',
        "args": ['ACTION_384_sequence_looping_on_0']
    }
]
