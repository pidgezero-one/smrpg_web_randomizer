from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_597_object_memory_clear_bit_0',
        "command": 'object_memory_clear_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_597_set_sprite_sequence_1',
        "command": 'set_sprite_sequence',
        "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_597_shadow_on_2',
        "command": 'shadow_on'
    },
    {
        "identifier": 'ACTION_597_set_vram_priority_3',
        "command": 'set_vram_priority',
        "args": [VramPriority.PRIORITY_3]
    },
    {
        "identifier": 'ACTION_597_set_priority_4',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_597_db_5',
        "command": 'db',
        "args": [0xc8, 0x00]
    },
    {
        "identifier": 'ACTION_597_add_short_6',
        "command": 'add_short',
        "args": [0x7016, 0xf600]
    },
    {
        "identifier": 'ACTION_597_add_short_7',
        "command": 'add_short',
        "args": [0x7018, 0x0500]
    },
    {
        "identifier": 'ACTION_597_set_short_8',
        "command": 'set_short',
        "args": [0x701a, 0x0000]
    },
    {
        "identifier": 'ACTION_597_db_9',
        "command": 'db',
        "args": [0x99]
    },
    {
        "identifier": 'ACTION_597_visibility_on_10',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_597_set_animation_speed_11',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_597_set_animation_speed_12',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_597_set_sprite_sequence_13',
        "command": 'set_sprite_sequence',
        "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_597_shift_northeast_steps_14',
        "command": 'shift_northeast_steps',
        "args": [4]
    },
    {
        "identifier": 'ACTION_597_play_sound_15',
        "command": 'play_sound',
        "args": [Sounds._050_WATER_DROPLET, 4]
    },
    {
        "identifier": 'ACTION_597_pause_16',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_597_reset_properties_17',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_597_fixed_f_coord_on_18',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_597_set_animation_speed_19',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_597_set_animation_speed_20',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_597_add_z_coord_1_step_21',
        "command": 'add_z_coord_1_step'
    },
    {
        "identifier": 'ACTION_597_set_animation_speed_22',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_597_shift_z_up_pixels_23',
        "command": 'shift_z_up_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_597_set_animation_speed_24',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_597_shift_z_up_pixels_25',
        "command": 'shift_z_up_pixels',
        "args": [4]
    },
    {
        "identifier": 'ACTION_597_set_animation_speed_26',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_597_shift_z_up_pixels_27',
        "command": 'shift_z_up_pixels',
        "args": [2]
    },
    {
        "identifier": 'ACTION_597_start_loop_n_times_28',
        "command": 'start_loop_n_times',
        "args": [1]
    },
    {
        "identifier": 'ACTION_597_shift_z_down_pixels_29',
        "command": 'shift_z_down_pixels',
        "args": [2]
    },
    {
        "identifier": 'ACTION_597_shift_z_up_pixels_30',
        "command": 'shift_z_up_pixels',
        "args": [2]
    },
    {
        "identifier": 'ACTION_597_end_loop_31',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_597_set_animation_speed_32',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_597_shift_northeast_pixels_33',
        "command": 'shift_northeast_pixels',
        "args": [4]
    },
    {
        "identifier": 'ACTION_597_shift_z_down_pixels_34',
        "command": 'shift_z_down_pixels',
        "args": [12]
    },
    {
        "identifier": 'ACTION_597_dec_z_coord_1_step_35',
        "command": 'dec_z_coord_1_step'
    },
    {
        "identifier": 'ACTION_597_visibility_off_36',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_597_ret_37',
        "command": 'ret'
    }
]
