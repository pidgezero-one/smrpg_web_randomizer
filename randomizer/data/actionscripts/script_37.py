from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_37_set_priority_0',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_37_sequence_looping_on_1',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_37_pause_2',
        "command": 'pause',
        "args": [40]
    },
    {
        "identifier": 'ACTION_37_shift_southeast_steps_3',
        "command": 'shift_southeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_37_set_animation_speed_4',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_37_jump_to_height_5',
        "command": 'jump_to_height',
        "args": [96]
    },
    {
        "identifier": 'ACTION_37_shift_southeast_steps_6',
        "command": 'shift_southeast_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_37_set_animation_speed_7',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_37_fixed_f_coord_on_8',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_37_walk_1_step_east_9',
        "command": 'walk_1_step_east'
    },
    {
        "identifier": 'ACTION_37_fixed_f_coord_off_10',
        "command": 'fixed_f_coord_off'
    },
    {
        "identifier": 'ACTION_37_walk_1_step_northeast_11',
        "command": 'walk_1_step_northeast'
    },
    {
        "identifier": 'ACTION_37_set_animation_speed_12',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_37_start_loop_n_times_13',
        "command": 'start_loop_n_times',
        "args": [1]
    },
    {
        "identifier": 'ACTION_37_shift_z_up_pixels_14',
        "command": 'shift_z_up_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_37_shift_z_down_pixels_15',
        "command": 'shift_z_down_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_37_end_loop_16',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_37_set_bit_17',
        "command": 'set_bit',
        "args": [0x7043, 2]
    },
    {
        "identifier": 'ACTION_37_set_vram_priority_18',
        "command": 'set_vram_priority',
        "args": [VramPriority.PRIORITY_3]
    },
    {
        "identifier": 'ACTION_37_set_animation_speed_19',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_37_walk_1_step_west_20',
        "command": 'walk_1_step_west'
    },
    {
        "identifier": 'ACTION_37_jump_to_height_21',
        "command": 'jump_to_height',
        "args": [96]
    },
    {
        "identifier": 'ACTION_37_shift_northwest_steps_22',
        "command": 'shift_northwest_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_37_set_animation_speed_23',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_37_shift_northwest_steps_24',
        "command": 'shift_northwest_steps',
        "args": [4]
    },
    {
        "identifier": 'ACTION_37_play_sound_25',
        "command": 'play_sound',
        "args": [Sounds._065_THWOMP_STOMP, 4]
    },
    {
        "identifier": 'ACTION_37_set_animation_speed_26',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_37_set_sprite_sequence_27',
        "command": 'set_sprite_sequence',
        "args": [2, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF]]
    },
    {
        "identifier": 'ACTION_37_pause_28',
        "command": 'pause',
        "args": [40]
    },
    {
        "identifier": 'ACTION_37_set_animation_speed_29',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_37_shift_west_steps_30',
        "command": 'shift_west_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_37_shift_northwest_steps_31',
        "command": 'shift_northwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_37_set_animation_speed_32',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_37_jump_to_height_33',
        "command": 'jump_to_height',
        "args": [96]
    },
    {
        "identifier": 'ACTION_37_shift_northwest_steps_34',
        "command": 'shift_northwest_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_37_set_animation_speed_35',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_37_shift_northwest_steps_36',
        "command": 'shift_northwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_37_object_memory_modify_bits_37',
        "command": 'object_memory_modify_bits',
        "args": [0x09, [5], [4, 6]]
    },
    {
        "identifier": 'ACTION_37_shift_northwest_steps_38',
        "command": 'shift_northwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_37_set_priority_39',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_37_walk_1_step_northwest_40',
        "command": 'walk_1_step_northwest'
    },
    {
        "identifier": 'ACTION_37_set_bit_41',
        "command": 'set_bit',
        "args": [0x7043, 3]
    },
    {
        "identifier": 'ACTION_37_ret_42',
        "command": 'ret'
    }
]
