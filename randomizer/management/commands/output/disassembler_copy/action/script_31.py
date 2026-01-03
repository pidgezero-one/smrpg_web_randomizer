
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_31_start_loop_n_times_0',
        "command": 'start_loop_n_times',
        "args": [1]
    },
    {
        "identifier": 'ACTION_31_set_sprite_sequence_1',
        "command": 'set_sprite_sequence',
        "args": [0, 5, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_31_pause_2',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'ACTION_31_set_sprite_sequence_3',
        "command": 'set_sprite_sequence',
        "args": [1, 5, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_31_pause_4',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_31_set_sprite_sequence_5',
        "command": 'set_sprite_sequence',
        "args": [2, 5, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_31_pause_6',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_31_set_sprite_sequence_7',
        "command": 'set_sprite_sequence',
        "args": [3, 5, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_31_pause_8',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_31_set_sprite_sequence_9',
        "command": 'set_sprite_sequence',
        "args": [4, 5, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_31_play_sound_10',
        "command": 'play_sound',
        "args": [Sounds._057_FINGER_SNAP, 4]
    },
    {
        "identifier": 'ACTION_31_pause_11',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_31_set_sprite_sequence_12',
        "command": 'set_sprite_sequence',
        "args": [3, 5, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_31_pause_13',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'ACTION_31_set_sprite_sequence_14',
        "command": 'set_sprite_sequence',
        "args": [4, 5, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_31_pause_15',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'ACTION_31_set_sprite_sequence_16',
        "command": 'set_sprite_sequence',
        "args": [2, 5, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_31_pause_17',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'ACTION_31_end_loop_18',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_31_reset_properties_19',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_31_pause_20',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_31_face_southeast_21',
        "command": 'face_southeast'
    },
    {
        "identifier": 'ACTION_31_pause_22',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_31_face_southwest_23',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_31_set_bit_24',
        "command": 'set_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'ACTION_31_pause_25',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_31_set_animation_speed_26',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_31_set_animation_speed_27',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_31_fixed_f_coord_on_28',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_31_shift_northeast_pixels_29',
        "command": 'shift_northeast_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_31_clear_bit_30',
        "command": 'clear_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'ACTION_31_shift_northeast_pixels_31',
        "command": 'shift_northeast_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_31_shift_northeast_steps_32',
        "command": 'shift_northeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_31_sequence_looping_off_33',
        "command": 'sequence_looping_off'
    },
    {
        "identifier": 'ACTION_31_pause_34',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'ACTION_31_set_animation_speed_35',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_31_shift_southwest_pixels_36',
        "command": 'shift_southwest_pixels',
        "args": [2]
    },
    {
        "identifier": 'ACTION_31_play_sound_37',
        "command": 'play_sound',
        "args": [Sounds._022_CLOSE_DOOR, 4]
    },
    {
        "identifier": 'ACTION_31_start_loop_n_times_38',
        "command": 'start_loop_n_times',
        "args": [3]
    },
    {
        "identifier": 'ACTION_31_shift_northeast_pixels_39',
        "command": 'shift_northeast_pixels',
        "args": [4]
    },
    {
        "identifier": 'ACTION_31_shift_southwest_pixels_40',
        "command": 'shift_southwest_pixels',
        "args": [4]
    },
    {
        "identifier": 'ACTION_31_end_loop_41',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_31_shift_northeast_pixels_42',
        "command": 'shift_northeast_pixels',
        "args": [2]
    },
    {
        "identifier": 'ACTION_31_set_animation_speed_43',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_31_set_animation_speed_44',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_31_set_sprite_sequence_45',
        "command": 'set_sprite_sequence',
        "args": [13, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_31_pause_46',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_31_reset_properties_47',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_31_shift_southwest_steps_48',
        "command": 'shift_southwest_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_31_face_northeast_49',
        "command": 'face_northeast'
    },
    {
        "identifier": 'ACTION_31_pause_50',
        "command": 'pause',
        "args": [40]
    },
    {
        "identifier": 'ACTION_31_jmp_51',
        "command": 'jmp',
        "args": ['ACTION_31_start_loop_n_times_0']
    }
]
