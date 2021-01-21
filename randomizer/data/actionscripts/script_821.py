from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_821_set_solidity_bits_0',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.BIT_4]]
    },
    {
        "identifier": 'ACTION_821_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_821_fixed_f_coord_on_2',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_821_set_700C_to_pressed_button_3',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_821_jmp_if_var_equals_short_4',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 27, 'ACTION_821_set_animation_speed_28']
    },
    {
        "identifier": 'ACTION_821_jmp_if_var_equals_short_5',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 21, 'ACTION_821_shift_southwest_steps_19']
    },
    {
        "identifier": 'ACTION_821_set_priority_6',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_821_add_7',
        "command": 'add',
        "args": [0x700c, 65515]
    },
    {
        "identifier": 'ACTION_821_add_8',
        "command": 'add',
        "args": [0x700c, 0x01]
    },
    {
        "identifier": 'ACTION_821_load_mem_9',
        "command": 'load_mem',
        "args": [0x700c]
    },
    {
        "identifier": 'ACTION_821_pause_10',
        "command": 'pause',
        "args": [9]
    },
    {
        "identifier": 'ACTION_821_end_loop_11',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_821_set_700C_to_pressed_button_12',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_821_mem_700C_and_const_13',
        "command": 'mem_700C_and_const',
        "args": [0x0001]
    },
    {
        "identifier": 'ACTION_821_jmp_if_var_equals_short_14',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 0, 'ACTION_821_shift_z_up_steps_16']
    },
    {
        "identifier": 'ACTION_821_pause_15',
        "command": 'pause',
        "args": [96]
    },
    {
        "identifier": 'ACTION_821_shift_z_up_steps_16',
        "command": 'shift_z_up_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_821_shift_z_down_steps_17',
        "command": 'shift_z_down_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_821_jmp_18',
        "command": 'jmp',
        "args": ['ACTION_821_shift_z_up_steps_16']
    },
    {
        "identifier": 'ACTION_821_shift_southwest_steps_19',
        "command": 'shift_southwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_821_shift_z_up_steps_20',
        "command": 'shift_z_up_steps',
        "args": [5]
    },
    {
        "identifier": 'ACTION_821_walk_1_step_southwest_21',
        "command": 'walk_1_step_southwest'
    },
    {
        "identifier": 'ACTION_821_pause_22',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'ACTION_821_walk_1_step_northeast_23',
        "command": 'walk_1_step_northeast'
    },
    {
        "identifier": 'ACTION_821_shift_z_down_steps_24',
        "command": 'shift_z_down_steps',
        "args": [5]
    },
    {
        "identifier": 'ACTION_821_shift_northeast_steps_25',
        "command": 'shift_northeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_821_pause_26',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'ACTION_821_jmp_27',
        "command": 'jmp',
        "args": ['ACTION_821_shift_southwest_steps_19']
    },
    {
        "identifier": 'ACTION_821_set_animation_speed_28',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_821_shift_z_up_steps_29',
        "command": 'shift_z_up_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_821_set_animation_speed_30',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_821_shift_z_up_steps_31',
        "command": 'shift_z_up_steps',
        "args": [4]
    },
    {
        "identifier": 'ACTION_821_set_animation_speed_32',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_821_shift_z_up_steps_33',
        "command": 'shift_z_up_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_821_start_loop_n_times_34',
        "command": 'start_loop_n_times',
        "args": [7]
    },
    {
        "identifier": 'ACTION_821_shift_z_down_pixels_35',
        "command": 'shift_z_down_pixels',
        "args": [4]
    },
    {
        "identifier": 'ACTION_821_shift_z_up_pixels_36',
        "command": 'shift_z_up_pixels',
        "args": [4]
    },
    {
        "identifier": 'ACTION_821_end_loop_37',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_821_set_animation_speed_38',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_821_shift_z_down_steps_39',
        "command": 'shift_z_down_steps',
        "args": [10]
    },
    {
        "identifier": 'ACTION_821_jmp_40',
        "command": 'jmp',
        "args": ['ACTION_821_set_animation_speed_28']
    }
]
