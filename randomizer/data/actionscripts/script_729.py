from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_729_visibility_off_0',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_729_pause_1',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_729_jmp_if_bit_clear_2',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 4, 'ACTION_729_visibility_off_0']
    },
    {
        "identifier": 'ACTION_729_visibility_on_3',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_729_sequence_looping_on_4',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_729_play_sound_5',
        "command": 'play_sound',
        "args": [Sounds._089_LIT_FUSE, 4]
    },
    {
        "identifier": 'ACTION_729_sequence_playback_on_6',
        "command": 'sequence_playback_on'
    },
    {
        "identifier": 'ACTION_729_set_sprite_sequence_7',
        "command": 'set_sprite_sequence',
        "args": [2, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_729_pause_8',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'ACTION_729_set_sprite_sequence_9',
        "command": 'set_sprite_sequence',
        "args": [3, 0, [_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_729_pause_10',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'ACTION_729_visibility_off_11',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_729_db_12',
        "command": 'db',
        "args": [0xc7, 0x07]
    },
    {
        "identifier": 'ACTION_729_start_loop_n_times_13',
        "command": 'start_loop_n_times',
        "args": [2]
    },
    {
        "identifier": 'ACTION_729_add_short_14',
        "command": 'add_short',
        "args": [0x7014, 0x0020]
    },
    {
        "identifier": 'ACTION_729_jump_to_subroutine_15',
        "command": 'jump_to_subroutine',
        "args": [0x87fb]
    },
    {
        "identifier": 'ACTION_729_create_packet_at_7010_coords_jmp_if_null_16',
        "command": 'create_packet_at_7010_coords_jmp_if_null',
        "args": [NPCPackets._024_BOMB_EXPLOSION_SFX, 'ACTION_729_pause_38']
    },
    {
        "identifier": 'ACTION_729_add_short_17',
        "command": 'add_short',
        "args": [0x7014, 0x0020]
    },
    {
        "identifier": 'ACTION_729_add_short_18',
        "command": 'add_short',
        "args": [0x7010, 0x0040]
    },
    {
        "identifier": 'ACTION_729_pause_19',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'ACTION_729_jump_to_subroutine_20',
        "command": 'jump_to_subroutine',
        "args": [0x87fb]
    },
    {
        "identifier": 'ACTION_729_create_packet_at_7010_coords_jmp_if_null_21',
        "command": 'create_packet_at_7010_coords_jmp_if_null',
        "args": [NPCPackets._024_BOMB_EXPLOSION_SFX, 'ACTION_729_pause_38']
    },
    {
        "identifier": 'ACTION_729_add_short_22',
        "command": 'add_short',
        "args": [0x7014, 0x0020]
    },
    {
        "identifier": 'ACTION_729_add_short_23',
        "command": 'add_short',
        "args": [0x7010, 0xff80]
    },
    {
        "identifier": 'ACTION_729_pause_24',
        "command": 'pause',
        "args": [11]
    },
    {
        "identifier": 'ACTION_729_jump_to_subroutine_25',
        "command": 'jump_to_subroutine',
        "args": [0x87fb]
    },
    {
        "identifier": 'ACTION_729_create_packet_at_7010_coords_jmp_if_null_26',
        "command": 'create_packet_at_7010_coords_jmp_if_null',
        "args": [NPCPackets._024_BOMB_EXPLOSION_SFX, 'ACTION_729_pause_38']
    },
    {
        "identifier": 'ACTION_729_add_short_27',
        "command": 'add_short',
        "args": [0x7014, 0x0020]
    },
    {
        "identifier": 'ACTION_729_add_short_28',
        "command": 'add_short',
        "args": [0x7012, 0x0040]
    },
    {
        "identifier": 'ACTION_729_pause_29',
        "command": 'pause',
        "args": [9]
    },
    {
        "identifier": 'ACTION_729_jump_to_subroutine_30',
        "command": 'jump_to_subroutine',
        "args": [0x87fb]
    },
    {
        "identifier": 'ACTION_729_create_packet_at_7010_coords_jmp_if_null_31',
        "command": 'create_packet_at_7010_coords_jmp_if_null',
        "args": [NPCPackets._024_BOMB_EXPLOSION_SFX, 'ACTION_729_pause_38']
    },
    {
        "identifier": 'ACTION_729_add_short_32',
        "command": 'add_short',
        "args": [0x7014, 0x0020]
    },
    {
        "identifier": 'ACTION_729_add_short_33',
        "command": 'add_short',
        "args": [0x7012, 0xffc0]
    },
    {
        "identifier": 'ACTION_729_add_short_34',
        "command": 'add_short',
        "args": [0x7010, 0x0040]
    },
    {
        "identifier": 'ACTION_729_pause_35',
        "command": 'pause',
        "args": [11]
    },
    {
        "identifier": 'ACTION_729_jump_to_subroutine_36',
        "command": 'jump_to_subroutine',
        "args": [0x87fb]
    },
    {
        "identifier": 'ACTION_729_create_packet_at_7010_coords_jmp_if_null_37',
        "command": 'create_packet_at_7010_coords_jmp_if_null',
        "args": [NPCPackets._024_BOMB_EXPLOSION_SFX, 'ACTION_729_pause_38']
    },
    {
        "identifier": 'ACTION_729_pause_38',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'ACTION_729_end_loop_39',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_729_set_bit_40',
        "command": 'set_bit',
        "args": [0x7043, 5]
    },
    {
        "identifier": 'ACTION_729_ret_41',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_729_pause_42',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_729_jmp_if_bit_set_43',
        "command": 'jmp_if_bit_set',
        "args": [0x707c, 4, 'ACTION_729_pause_42']
    },
    {
        "identifier": 'ACTION_729_ret_44',
        "command": 'ret'
    }
]
