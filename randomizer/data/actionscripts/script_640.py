from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_640_set_priority_0',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_640_set_vram_priority_1',
        "command": 'set_vram_priority',
        "args": [VramPriority.NORMAL]
    },
    {
        "identifier": 'ACTION_640_sequence_looping_on_2',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_640_fixed_f_coord_on_3',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_640_start_loop_n_times_4',
        "command": 'start_loop_n_times',
        "args": [5]
    },
    {
        "identifier": 'ACTION_640_set_animation_speed_5',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_640_walk_1_step_northeast_6',
        "command": 'walk_1_step_northeast'
    },
    {
        "identifier": 'ACTION_640_set_animation_speed_7',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_640_jump_to_height_8',
        "command": 'jump_to_height',
        "args": [56]
    },
    {
        "identifier": 'ACTION_640_pause_9',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'ACTION_640_jump_to_height_10',
        "command": 'jump_to_height',
        "args": [56]
    },
    {
        "identifier": 'ACTION_640_pause_11',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'ACTION_640_set_animation_speed_12',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_640_walk_1_step_southwest_13',
        "command": 'walk_1_step_southwest'
    },
    {
        "identifier": 'ACTION_640_end_loop_14',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_640_set_animation_speed_15',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_640_walk_1_step_northeast_16',
        "command": 'walk_1_step_northeast'
    },
    {
        "identifier": 'ACTION_640_pause_17',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_640_jmp_if_bit_clear_18',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 1, 'ACTION_640_pause_17']
    },
    {
        "identifier": 'ACTION_640_set_animation_speed_19',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_640_walk_1_step_southwest_20',
        "command": 'walk_1_step_southwest'
    },
    {
        "identifier": 'ACTION_640_start_loop_n_times_21',
        "command": 'start_loop_n_times',
        "args": [7]
    },
    {
        "identifier": 'ACTION_640_shift_z_up_pixels_22',
        "command": 'shift_z_up_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_640_shift_z_down_pixels_23',
        "command": 'shift_z_down_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_640_end_loop_24',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_640_set_animation_speed_25',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_640_set_animation_speed_26',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_640_start_loop_n_times_27',
        "command": 'start_loop_n_times',
        "args": [5]
    },
    {
        "identifier": 'ACTION_640_jump_to_height_28',
        "command": 'jump_to_height',
        "args": [56]
    },
    {
        "identifier": 'ACTION_640_walk_1_step_northeast_29',
        "command": 'walk_1_step_northeast'
    },
    {
        "identifier": 'ACTION_640_jump_to_height_30',
        "command": 'jump_to_height',
        "args": [56]
    },
    {
        "identifier": 'ACTION_640_walk_1_step_southwest_31',
        "command": 'walk_1_step_southwest'
    },
    {
        "identifier": 'ACTION_640_end_loop_32',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_640_shift_northeast_steps_33',
        "command": 'shift_northeast_steps',
        "args": [5]
    },
    {
        "identifier": 'ACTION_640_walk_1_step_east_34',
        "command": 'walk_1_step_east'
    },
    {
        "identifier": 'ACTION_640_ret_35',
        "command": 'ret'
    }
]
