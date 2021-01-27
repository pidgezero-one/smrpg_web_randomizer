from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_937_shadow_off_0',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_937_sequence_looping_on_1',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_937_set_priority_2',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_937_db_3',
        "command": 'db',
        "args": [0x20, 0x07]
    },
    {
        "identifier": 'ACTION_937_set_700C_to_pressed_button_4',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_937_jmp_if_700C_equals_short_5',
        "command": 'jmp_if_700C_equals_short',
        "args": [26, 'ACTION_937_fixed_f_coord_on_9']
    },
    {
        "identifier": 'ACTION_937_jmp_if_700C_equals_short_6',
        "command": 'jmp_if_700C_equals_short',
        "args": [27, 'ACTION_937_fixed_f_coord_on_16']
    },
    {
        "identifier": 'ACTION_937_jmp_if_700C_equals_short_7',
        "command": 'jmp_if_700C_equals_short',
        "args": [28, 'ACTION_937_embedded_animation_routine_23']
    },
    {
        "identifier": 'ACTION_937_jmp_if_700C_equals_short_8',
        "command": 'jmp_if_700C_equals_short',
        "args": [29, 'ACTION_937_embedded_animation_routine_27']
    },
    {
        "identifier": 'ACTION_937_fixed_f_coord_on_9',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_937_shift_northeast_pixels_10',
        "command": 'shift_northeast_pixels',
        "args": [6]
    },
    {
        "identifier": 'ACTION_937_shift_z_down_pixels_11',
        "command": 'shift_z_down_pixels',
        "args": [5]
    },
    {
        "identifier": 'ACTION_937_embedded_animation_routine_12',
        "command": 'embedded_animation_routine',
        "args": [0x26, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x60, 0x00, 0x01, 0xd0, 0xff, 0x80, 0x01, 0x80]
    },
    {
        "identifier": 'ACTION_937_embedded_animation_routine_13',
        "command": 'embedded_animation_routine',
        "args": [0x27, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x34, 0x00, 0x01, 0xe6, 0xff, 0x20, 0x01, 0x80]
    },
    {
        "identifier": 'ACTION_937_embedded_animation_routine_14',
        "command": 'embedded_animation_routine',
        "args": [0x28, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x04, 0x00, 0x01, 0x00, 0x00, 0x00, 0x02, 0x80]
    },
    {
        "identifier": 'ACTION_937_jmp_15',
        "command": 'jmp',
        "args": ['ACTION_937_pause_short_30']
    },
    {
        "identifier": 'ACTION_937_fixed_f_coord_on_16',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_937_shift_northeast_pixels_17',
        "command": 'shift_northeast_pixels',
        "args": [6]
    },
    {
        "identifier": 'ACTION_937_shift_z_down_pixels_18',
        "command": 'shift_z_down_pixels',
        "args": [3]
    },
    {
        "identifier": 'ACTION_937_embedded_animation_routine_19',
        "command": 'embedded_animation_routine',
        "args": [0x26, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x70, 0x00, 0x01, 0xc3, 0xff, 0x00, 0x02, 0x80]
    },
    {
        "identifier": 'ACTION_937_embedded_animation_routine_20',
        "command": 'embedded_animation_routine',
        "args": [0x27, 0x00, 0x00, 0x00, 0x00, 0x00, 0x40, 0x00, 0x38, 0x00, 0x01, 0xe2, 0xff, 0xc0, 0x00, 0x80]
    },
    {
        "identifier": 'ACTION_937_embedded_animation_routine_21',
        "command": 'embedded_animation_routine',
        "args": [0x28, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x04, 0x00, 0x01, 0x00, 0x00, 0x00, 0x01, 0x80]
    },
    {
        "identifier": 'ACTION_937_jmp_22',
        "command": 'jmp',
        "args": ['ACTION_937_pause_short_30']
    },
    {
        "identifier": 'ACTION_937_embedded_animation_routine_23',
        "command": 'embedded_animation_routine',
        "args": [0x26, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x50, 0x00, 0x01, 0xd1, 0xff, 0x40, 0x02, 0x80]
    },
    {
        "identifier": 'ACTION_937_embedded_animation_routine_24',
        "command": 'embedded_animation_routine',
        "args": [0x27, 0x00, 0x00, 0x00, 0x00, 0x00, 0x80, 0x00, 0x30, 0x00, 0x01, 0xe4, 0xff, 0x00, 0x01, 0x80]
    },
    {
        "identifier": 'ACTION_937_embedded_animation_routine_25',
        "command": 'embedded_animation_routine',
        "args": [0x28, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x04, 0x00, 0x01, 0x00, 0x00, 0x00, 0x03, 0x80]
    },
    {
        "identifier": 'ACTION_937_jmp_26',
        "command": 'jmp',
        "args": ['ACTION_937_pause_short_30']
    },
    {
        "identifier": 'ACTION_937_embedded_animation_routine_27',
        "command": 'embedded_animation_routine',
        "args": [0x26, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x68, 0x00, 0x01, 0xc5, 0xff, 0x00, 0x01, 0x80]
    },
    {
        "identifier": 'ACTION_937_embedded_animation_routine_28',
        "command": 'embedded_animation_routine',
        "args": [0x27, 0x00, 0x00, 0x00, 0x00, 0x00, 0xc0, 0x00, 0x50, 0x00, 0x01, 0xd3, 0xff, 0x80, 0x01, 0x80]
    },
    {
        "identifier": 'ACTION_937_embedded_animation_routine_29',
        "command": 'embedded_animation_routine',
        "args": [0x28, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x04, 0x00, 0x01, 0x00, 0x00, 0x00, 0x03, 0x80]
    },
    {
        "identifier": 'ACTION_937_pause_short_30',
        "command": 'pause_short',
        "args": [500]
    },
    {
        "identifier": 'ACTION_937_start_loop_n_times_31',
        "command": 'start_loop_n_times',
        "args": [9]
    },
    {
        "identifier": 'ACTION_937_visibility_off_32',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_937_pause_33',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'ACTION_937_visibility_on_34',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_937_pause_35',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'ACTION_937_end_loop_36',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_937_start_loop_n_times_37',
        "command": 'start_loop_n_times',
        "args": [9]
    },
    {
        "identifier": 'ACTION_937_visibility_off_38',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_937_pause_39',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_937_visibility_on_40',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_937_pause_41',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_937_end_loop_42',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_937_start_loop_n_times_43',
        "command": 'start_loop_n_times',
        "args": [9]
    },
    {
        "identifier": 'ACTION_937_visibility_off_44',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_937_pause_45',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_937_visibility_on_46',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_937_pause_47',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_937_end_loop_48',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_937_visibility_off_49',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_937_ret_50',
        "command": 'ret'
    }
]
