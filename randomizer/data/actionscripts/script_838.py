from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_838_sequence_looping_on_0',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_838_clear_solidity_bits_1',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_838_shift_northeast_pixels_2',
        "command": 'shift_northeast_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_838_set_animation_speed_3',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_838_walk_1_step_northeast_4',
        "command": 'walk_1_step_northeast'
    },
    {
        "identifier": 'ACTION_838_jump_to_height_silent_5',
        "command": 'jump_to_height_silent',
        "args": [108]
    },
    {
        "identifier": 'ACTION_838_shift_northeast_steps_6',
        "command": 'shift_northeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_838_shift_northeast_pixels_7',
        "command": 'shift_northeast_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_838_shift_northeast_steps_8',
        "command": 'shift_northeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_838_shift_northwest_pixels_9',
        "command": 'shift_northwest_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_838_jump_to_height_silent_10',
        "command": 'jump_to_height_silent',
        "args": [108]
    },
    {
        "identifier": 'ACTION_838_shift_northwest_steps_11',
        "command": 'shift_northwest_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_838_shift_northwest_pixels_12',
        "command": 'shift_northwest_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_838_walk_1_step_northeast_13',
        "command": 'walk_1_step_northeast'
    },
    {
        "identifier": 'ACTION_838_shift_northeast_pixels_14',
        "command": 'shift_northeast_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_838_set_bit_15',
        "command": 'set_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'ACTION_838_walk_1_step_northwest_16',
        "command": 'walk_1_step_northwest'
    },
    {
        "identifier": 'ACTION_838_shift_northwest_pixels_17',
        "command": 'shift_northwest_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_838_jump_to_height_silent_18',
        "command": 'jump_to_height_silent',
        "args": [108]
    },
    {
        "identifier": 'ACTION_838_shift_northwest_steps_19',
        "command": 'shift_northwest_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_838_shift_northwest_steps_20',
        "command": 'shift_northwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_838_set_animation_speed_21',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_838_set_sprite_sequence_22',
        "command": 'set_sprite_sequence',
        "args": [3, 2, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_838_pause_23',
        "command": 'pause',
        "args": [48]
    },
    {
        "identifier": 'ACTION_838_reset_properties_24',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_838_set_animation_speed_25',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_838_walk_1_step_southeast_26',
        "command": 'walk_1_step_southeast'
    },
    {
        "identifier": 'ACTION_838_shift_southeast_pixels_27',
        "command": 'shift_southeast_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_838_pause_28',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'ACTION_838_face_southwest_29',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_838_pause_30',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'ACTION_838_shift_north_pixels_31',
        "command": 'shift_north_pixels',
        "args": [4]
    },
    {
        "identifier": 'ACTION_838_jump_to_height_silent_32',
        "command": 'jump_to_height_silent',
        "args": [108]
    },
    {
        "identifier": 'ACTION_838_shift_northwest_steps_33',
        "command": 'shift_northwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_838_shift_northwest_pixels_34',
        "command": 'shift_northwest_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_838_pause_35',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_838_jump_to_height_silent_36',
        "command": 'jump_to_height_silent',
        "args": [108]
    },
    {
        "identifier": 'ACTION_838_shift_northwest_steps_37',
        "command": 'shift_northwest_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_838_pause_38',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'ACTION_838_face_west_39',
        "command": 'face_west'
    },
    {
        "identifier": 'ACTION_838_pause_40',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'ACTION_838_face_southwest_41',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_838_pause_42',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'ACTION_838_set_sprite_sequence_43',
        "command": 'set_sprite_sequence',
        "args": [3, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_838_pause_44',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'ACTION_838_set_bit_45',
        "command": 'set_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'ACTION_838_db_46',
        "command": 'db',
        "args": [0x20, 0x07]
    },
    {
        "identifier": 'ACTION_838_db_47',
        "command": 'db',
        "args": [0x24, 0x30, 0xfe, 0x00, 0x02]
    },
    {
        "identifier": 'ACTION_838_db_48',
        "command": 'db',
        "args": [0x25, 0xc0, 0x06, 0x80, 0xff]
    },
    {
        "identifier": 'ACTION_838_pause_49',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'ACTION_838_bpl_26_27_28_50',
        "command": 'bpl_26_27_28'
    },
    {
        "identifier": 'ACTION_838_sequence_looping_off_51',
        "command": 'sequence_looping_off'
    },
    {
        "identifier": 'ACTION_838_ret_52',
        "command": 'ret'
    }
]
