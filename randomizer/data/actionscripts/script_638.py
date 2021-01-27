from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_638_pause_0',
        "command": 'pause',
        "args": [59]
    },
    {
        "identifier": 'ACTION_638_visibility_on_1',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_638_transfer_to_xyzf_2',
        "command": 'transfer_to_xyzf',
        "args": [11, 49, 0, RadialDirections.SOUTHEAST]
    },
    {
        "identifier": 'ACTION_638_shift_xy_pixels_3',
        "command": 'shift_xy_pixels',
        "args": [8, 253]
    },
    {
        "identifier": 'ACTION_638_set_bit_4',
        "command": 'set_bit',
        "args": [0x7044, 3]
    },
    {
        "identifier": 'ACTION_638_db_5',
        "command": 'db',
        "args": [0x20, 0x04]
    },
    {
        "identifier": 'ACTION_638_db_6',
        "command": 'db',
        "args": [0x25, 0x00, 0x00, 0x72, 0xff]
    },
    {
        "identifier": 'ACTION_638_set_animation_speed_7',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_638_walk_1_step_northeast_8',
        "command": 'walk_1_step_northeast'
    },
    {
        "identifier": 'ACTION_638_shift_northeast_pixels_9',
        "command": 'shift_northeast_pixels',
        "args": [12]
    },
    {
        "identifier": 'ACTION_638_bpl_26_27_28_10',
        "command": 'bpl_26_27_28'
    },
    {
        "identifier": 'ACTION_638_play_sound_11',
        "command": 'play_sound',
        "args": [Sounds._033_JUMPING_BOUNCING_FISH, 4]
    },
    {
        "identifier": 'ACTION_638_start_loop_n_times_12',
        "command": 'start_loop_n_times',
        "args": [2]
    },
    {
        "identifier": 'ACTION_638_set_sprite_sequence_13',
        "command": 'set_sprite_sequence',
        "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_638_pause_14',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_638_set_sprite_sequence_15',
        "command": 'set_sprite_sequence',
        "args": [2, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_638_pause_16',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_638_set_sprite_sequence_17',
        "command": 'set_sprite_sequence',
        "args": [1, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_638_pause_18',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_638_end_loop_19',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_638_start_loop_n_times_20',
        "command": 'start_loop_n_times',
        "args": [1]
    },
    {
        "identifier": 'ACTION_638_visibility_off_21',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_638_pause_22',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_638_visibility_on_23',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_638_pause_24',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_638_set_sprite_sequence_25',
        "command": 'set_sprite_sequence',
        "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_638_pause_26',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_638_visibility_off_27',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_638_pause_28',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_638_visibility_on_29',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_638_pause_30',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_638_set_sprite_sequence_31',
        "command": 'set_sprite_sequence',
        "args": [2, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_638_pause_32',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_638_visibility_off_33',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_638_pause_34',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_638_visibility_on_35',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_638_pause_36',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_638_set_sprite_sequence_37',
        "command": 'set_sprite_sequence',
        "args": [1, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_638_pause_38',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_638_end_loop_39',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_638_visibility_off_40',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_638_pause_41',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_638_visibility_on_42',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_638_pause_43',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_638_set_sprite_sequence_44',
        "command": 'set_sprite_sequence',
        "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_638_pause_45',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_638_visibility_off_46',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_638_transfer_to_xyzf_47',
        "command": 'transfer_to_xyzf',
        "args": [22, 78, 0, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_638_clear_bit_48',
        "command": 'clear_bit',
        "args": [0x7044, 3]
    },
    {
        "identifier": 'ACTION_638_ret_49',
        "command": 'ret'
    }
]
