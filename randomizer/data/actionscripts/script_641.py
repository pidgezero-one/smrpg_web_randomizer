from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_641_set_priority_0',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_641_set_vram_priority_1',
        "command": 'set_vram_priority',
        "args": [VramPriority.NORMAL]
    },
    {
        "identifier": 'ACTION_641_sequence_looping_on_2',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_641_fixed_f_coord_on_3',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_641_pause_4',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_641_start_loop_n_times_5',
        "command": 'start_loop_n_times',
        "args": [5]
    },
    {
        "identifier": 'ACTION_641_set_animation_speed_6',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_641_walk_1_step_southwest_7',
        "command": 'walk_1_step_southwest'
    },
    {
        "identifier": 'ACTION_641_set_animation_speed_8',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_641_shift_southwest_pixels_9',
        "command": 'shift_southwest_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_641_shift_northeast_pixels_10',
        "command": 'shift_northeast_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_641_shift_southwest_pixels_11',
        "command": 'shift_southwest_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_641_shift_northeast_pixels_12',
        "command": 'shift_northeast_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_641_set_animation_speed_13',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_641_walk_1_step_northeast_14',
        "command": 'walk_1_step_northeast'
    },
    {
        "identifier": 'ACTION_641_end_loop_15',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_641_set_animation_speed_16',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_641_walk_1_step_southwest_17',
        "command": 'walk_1_step_southwest'
    },
    {
        "identifier": 'ACTION_641_pause_18',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_641_jmp_if_bit_clear_19',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 1, 'ACTION_641_pause_18']
    },
    {
        "identifier": 'ACTION_641_set_animation_speed_20',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_641_walk_1_step_northeast_21',
        "command": 'walk_1_step_northeast'
    },
    {
        "identifier": 'ACTION_641_start_loop_n_times_22',
        "command": 'start_loop_n_times',
        "args": [7]
    },
    {
        "identifier": 'ACTION_641_shift_z_up_pixels_23',
        "command": 'shift_z_up_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_641_shift_z_down_pixels_24',
        "command": 'shift_z_down_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_641_end_loop_25',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_641_set_animation_speed_26',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_641_set_animation_speed_27',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_641_pause_28',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'ACTION_641_start_loop_n_times_29',
        "command": 'start_loop_n_times',
        "args": [5]
    },
    {
        "identifier": 'ACTION_641_jump_to_height_30',
        "command": 'jump_to_height',
        "args": [56]
    },
    {
        "identifier": 'ACTION_641_walk_1_step_southeast_31',
        "command": 'walk_1_step_southeast'
    },
    {
        "identifier": 'ACTION_641_jump_to_height_32',
        "command": 'jump_to_height',
        "args": [56]
    },
    {
        "identifier": 'ACTION_641_walk_1_step_northwest_33',
        "command": 'walk_1_step_northwest'
    },
    {
        "identifier": 'ACTION_641_end_loop_34',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_641_shift_east_steps_35',
        "command": 'shift_east_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_641_ret_36',
        "command": 'ret'
    }
]
