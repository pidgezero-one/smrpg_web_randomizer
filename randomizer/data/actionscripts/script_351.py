from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_351_jmp_if_var_equals_byte_0',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70df, 50, 'ACTION_351_set_animation_speed_28']
    },
    {
        "identifier": 'ACTION_351_set_700C_to_current_level_1',
        "command": 'set_700C_to_current_level'
    },
    {
        "identifier": 'ACTION_351_jmp_if_700C_equals_short_2',
        "command": 'jmp_if_700C_equals_short',
        "args": [168, 'ACTION_351_db_19']
    },
    {
        "identifier": 'ACTION_351_visibility_off_3',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_351_shift_east_pixels_4',
        "command": 'shift_east_pixels',
        "args": [6]
    },
    {
        "identifier": 'ACTION_351_shift_z_up_pixels_5',
        "command": 'shift_z_up_pixels',
        "args": [5]
    },
    {
        "identifier": 'ACTION_351_reset_properties_6',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_351_pause_7',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'ACTION_351_visibility_on_8',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_351_set_sprite_sequence_9',
        "command": 'set_sprite_sequence',
        "args": [0, 0, [_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_351_pause_10',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'ACTION_351_play_sound_11',
        "command": 'play_sound',
        "args": [Sounds._118_BECKONING_TENTACLE, 4]
    },
    {
        "identifier": 'ACTION_351_pause_12',
        "command": 'pause',
        "args": [56]
    },
    {
        "identifier": 'ACTION_351_set_sprite_sequence_13',
        "command": 'set_sprite_sequence',
        "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_351_pause_14',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'ACTION_351_set_sprite_sequence_15',
        "command": 'set_sprite_sequence',
        "args": [2, 0, [_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_351_pause_16',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'ACTION_351_visibility_off_17',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_351_ret_18',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_351_db_19',
        "command": 'db',
        "args": [0xc8, 0x00]
    },
    {
        "identifier": 'ACTION_351_run_away_transfer_20',
        "command": 'run_away_transfer'
    },
    {
        "identifier": 'ACTION_351_set_priority_21',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_351_set_vram_priority_22',
        "command": 'set_vram_priority',
        "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
    },
    {
        "identifier": 'ACTION_351_visibility_on_23',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_351_pause_24',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_351_visibility_off_25',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_351_pause_26',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_351_jmp_27',
        "command": 'jmp',
        "args": ['ACTION_351_visibility_on_23']
    },
    {
        "identifier": 'ACTION_351_set_animation_speed_28',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_351_set_animation_speed_29',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_351_walk_1_step_f_direction_30',
        "command": 'walk_1_step_f_direction'
    },
    {
        "identifier": 'ACTION_351_turn_random_direction_31',
        "command": 'turn_random_direction'
    },
    {
        "identifier": 'ACTION_351_walk_1_step_f_direction_32',
        "command": 'walk_1_step_f_direction'
    },
    {
        "identifier": 'ACTION_351_jmp_if_random_above_128_33',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_351_set_animation_speed_28']
    },
    {
        "identifier": 'ACTION_351_face_mario_34',
        "command": 'face_mario'
    },
    {
        "identifier": 'ACTION_351_set_animation_speed_35',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_351_set_animation_speed_36',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_351_walk_1_step_f_direction_37',
        "command": 'walk_1_step_f_direction'
    },
    {
        "identifier": 'ACTION_351_jmp_38',
        "command": 'jmp',
        "args": ['ACTION_351_set_animation_speed_28']
    }
]
