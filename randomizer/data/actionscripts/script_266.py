from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_266_set_movement_bits_0',
        "command": 'set_movement_bits',
        "args": [[_0x0AFlags.BIT_0, _0x0AFlags.CANT_WALK_UNDER]]
    },
    {
        "identifier": 'ACTION_266_set_700C_to_pressed_button_1',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_266_mem_700C_and_const_2',
        "command": 'mem_700C_and_const',
        "args": [0x0003]
    },
    {
        "identifier": 'ACTION_266_jmp_if_700C_equals_short_3',
        "command": 'jmp_if_700C_equals_short',
        "args": [0, 'ACTION_266_set_animation_speed_9']
    },
    {
        "identifier": 'ACTION_266_jmp_if_700C_equals_short_4',
        "command": 'jmp_if_700C_equals_short',
        "args": [1, 'ACTION_266_pause_8']
    },
    {
        "identifier": 'ACTION_266_jmp_if_700C_equals_short_5',
        "command": 'jmp_if_700C_equals_short',
        "args": [2, 'ACTION_266_pause_7']
    },
    {
        "identifier": 'ACTION_266_pause_6',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'ACTION_266_pause_7',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'ACTION_266_pause_8',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'ACTION_266_set_animation_speed_9',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_266_sequence_playback_off_10',
        "command": 'sequence_playback_off'
    },
    {
        "identifier": 'ACTION_266_shift_z_down_steps_11',
        "command": 'shift_z_down_steps',
        "args": [4]
    },
    {
        "identifier": 'ACTION_266_face_mario_12',
        "command": 'face_mario'
    },
    {
        "identifier": 'ACTION_266_sequence_playback_on_13',
        "command": 'sequence_playback_on'
    },
    {
        "identifier": 'ACTION_266_clear_solidity_bits_14',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_266_set_animation_speed_15',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_266_set_solidity_bits_16',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_266_start_loop_n_times_17',
        "command": 'start_loop_n_times',
        "args": [31]
    },
    {
        "identifier": 'ACTION_266_shift_z_up_pixels_18',
        "command": 'shift_z_up_pixels',
        "args": [2]
    },
    {
        "identifier": 'ACTION_266_shift_f_direction_pixels_19',
        "command": 'shift_f_direction_pixels',
        "args": [1]
    },
    {
        "identifier": 'ACTION_266_end_loop_20',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_266_jmp_21',
        "command": 'jmp',
        "args": ['ACTION_266_set_animation_speed_9']
    }
]
