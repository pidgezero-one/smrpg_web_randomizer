from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_250_visibility_off_0',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_250_face_southeast_1',
        "command": 'face_southeast'
    },
    {
        "identifier": 'ACTION_250_transfer_to_xyzf_2',
        "command": 'transfer_to_xyzf',
        "args": [4, 19, 0, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_250_transfer_xyzf_pixels_3',
        "command": 'transfer_xyzf_pixels',
        "args": [12, 12, 0, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_250_shadow_on_4',
        "command": 'shadow_on'
    },
    {
        "identifier": 'ACTION_250_visibility_on_5',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_250_set_sprite_sequence_6',
        "command": 'set_sprite_sequence',
        "args": [9, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_250_pause_7',
        "command": 'pause',
        "args": [6]
    },
    {
        "identifier": 'ACTION_250_set_sprite_sequence_8',
        "command": 'set_sprite_sequence',
        "args": [8, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_250_pause_9',
        "command": 'pause',
        "args": [6]
    },
    {
        "identifier": 'ACTION_250_set_sprite_sequence_10',
        "command": 'set_sprite_sequence',
        "args": [7, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_250_pause_11',
        "command": 'pause',
        "args": [6]
    },
    {
        "identifier": 'ACTION_250_set_sprite_sequence_12',
        "command": 'set_sprite_sequence',
        "args": [6, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_250_pause_13',
        "command": 'pause',
        "args": [6]
    },
    {
        "identifier": 'ACTION_250_reset_properties_14',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_250_set_animation_speed_15',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_250_sequence_playback_on_16',
        "command": 'sequence_playback_on'
    },
    {
        "identifier": 'ACTION_250_shift_southeast_steps_17',
        "command": 'shift_southeast_steps',
        "args": [5]
    },
    {
        "identifier": 'ACTION_250_sequence_playback_off_18',
        "command": 'sequence_playback_off'
    },
    {
        "identifier": 'ACTION_250_add_z_coord_1_step_19',
        "command": 'add_z_coord_1_step'
    },
    {
        "identifier": 'ACTION_250_set_animation_speed_20',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_250_shift_z_up_steps_21',
        "command": 'shift_z_up_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_250_set_animation_speed_22',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_250_set_bit_23',
        "command": 'set_bit',
        "args": [0x7044, 4]
    },
    {
        "identifier": 'ACTION_250_shift_z_up_steps_24',
        "command": 'shift_z_up_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_250_set_animation_speed_25',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_250_shift_z_up_steps_26',
        "command": 'shift_z_up_steps',
        "args": [4]
    },
    {
        "identifier": 'ACTION_250_shadow_off_27',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_250_set_animation_speed_28',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_250_transfer_to_xyzf_29',
        "command": 'transfer_to_xyzf',
        "args": [3, 48, 0, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_250_set_bit_30',
        "command": 'set_bit',
        "args": [0x7044, 4]
    },
    {
        "identifier": 'ACTION_250_ret_31',
        "command": 'ret'
    }
]
