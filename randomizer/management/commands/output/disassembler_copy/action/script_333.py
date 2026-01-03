
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_333_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_333_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_333_add_z_coord_1_step_2',
        "command": 'add_z_coord_1_step'
    },
    {
        "identifier": 'ACTION_333_shift_z_down_pixels_3',
        "command": 'shift_z_down_pixels',
        "args": [15]
    },
    {
        "identifier": 'ACTION_333_set_bit_4',
        "command": 'set_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'ACTION_333_shift_z_down_pixels_5',
        "command": 'shift_z_down_pixels',
        "args": [1]
    },
    {
        "identifier": 'ACTION_333_set_animation_speed_6',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_333_shift_northeast_pixels_7',
        "command": 'shift_northeast_pixels',
        "args": [10]
    },
    {
        "identifier": 'ACTION_333_clear_bit_8',
        "command": 'clear_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'ACTION_333_shift_northeast_pixels_9',
        "command": 'shift_northeast_pixels',
        "args": [10]
    },
    {
        "identifier": 'ACTION_333_shift_northeast_steps_10',
        "command": 'shift_northeast_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_333_shift_northeast_pixels_11',
        "command": 'shift_northeast_pixels',
        "args": [11]
    },
    {
        "identifier": 'ACTION_333_set_sprite_sequence_12',
        "command": 'set_sprite_sequence',
        "args": [8, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_333_play_sound_13',
        "command": 'play_sound',
        "args": [Sounds._022_CLOSE_DOOR, 4]
    },
    {
        "identifier": 'ACTION_333_jump_to_height_silent_14',
        "command": 'jump_to_height_silent',
        "args": [88]
    },
    {
        "identifier": 'ACTION_333_shift_southwest_pixels_15',
        "command": 'shift_southwest_pixels',
        "args": [10]
    },
    {
        "identifier": 'ACTION_333_shift_southwest_steps_16',
        "command": 'shift_southwest_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_333_jump_to_height_silent_17',
        "command": 'jump_to_height_silent',
        "args": [80]
    },
    {
        "identifier": 'ACTION_333_set_animation_speed_18',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_333_shift_southwest_steps_19',
        "command": 'shift_southwest_steps',
        "args": [1]
    },
    {
        "identifier": 'ACTION_333_shift_southwest_pixels_20',
        "command": 'shift_southwest_pixels',
        "args": [5]
    },
    {
        "identifier": 'ACTION_333_face_northeast_21',
        "command": 'face_northeast'
    },
    {
        "identifier": 'ACTION_333_reset_properties_22',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_333_set_solidity_bits_23',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_333_set_animation_speed_24',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_333_pause_25',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'ACTION_333_clear_solidity_bits_26',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_333_jmp_if_bit_set_27',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 7, 'ACTION_333_ret_29']
    },
    {
        "identifier": 'ACTION_333_jmp_28',
        "command": 'jmp',
        "args": ['ACTION_333_set_animation_speed_0']
    },
    {
        "identifier": 'ACTION_333_ret_29',
        "command": 'ret'
    }
]
