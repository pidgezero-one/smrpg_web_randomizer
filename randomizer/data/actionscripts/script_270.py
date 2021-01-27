from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_270_set_movement_bits_0',
        "command": 'set_movement_bits',
        "args": [[_0x0AFlags.BIT_0, _0x0AFlags.CANT_WALK_UNDER]]
    },
    {
        "identifier": 'ACTION_270_set_priority_1',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_270_set_animation_speed_2',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_270_sequence_playback_off_3',
        "command": 'sequence_playback_off'
    },
    {
        "identifier": 'ACTION_270_shift_z_down_steps_4',
        "command": 'shift_z_down_steps',
        "args": [5]
    },
    {
        "identifier": 'ACTION_270_face_mario_5',
        "command": 'face_mario'
    },
    {
        "identifier": 'ACTION_270_set_700C_to_object_coord_6',
        "command": 'set_700C_to_object_coord',
        "args": [AreaObjects.DUMMY_0X07, Coords.F, []]
    },
    {
        "identifier": 'ACTION_270_set_7000_short_mem_to_700C_7',
        "command": 'set_7000_short_mem_to_700C',
        "args": [0x7032]
    },
    {
        "identifier": 'ACTION_270_sequence_playback_on_8',
        "command": 'sequence_playback_on'
    },
    {
        "identifier": 'ACTION_270_clear_solidity_bits_9',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_270_set_animation_speed_10',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_270_set_solidity_bits_11',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_270_start_loop_n_times_12',
        "command": 'start_loop_n_times',
        "args": [39]
    },
    {
        "identifier": 'ACTION_270_shift_z_up_pixels_13',
        "command": 'shift_z_up_pixels',
        "args": [2]
    },
    {
        "identifier": 'ACTION_270_shift_f_direction_pixels_14',
        "command": 'shift_f_direction_pixels',
        "args": [1]
    },
    {
        "identifier": 'ACTION_270_end_loop_15',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_270_jmp_16',
        "command": 'jmp',
        "args": ['ACTION_270_set_animation_speed_2']
    }
]
