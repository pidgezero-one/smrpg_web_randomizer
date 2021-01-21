from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_476_sequence_looping_on_0',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_476_set_700C_to_pressed_button_1',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_476_add_2',
        "command": 'add',
        "args": [0x700c, 65517]
    },
    {
        "identifier": 'ACTION_476_load_mem_3',
        "command": 'load_mem',
        "args": [0x700c]
    },
    {
        "identifier": 'ACTION_476_pause_4',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_476_end_loop_5',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_476_set_animation_speed_6',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_476_start_loop_n_times_7',
        "command": 'start_loop_n_times',
        "args": [2]
    },
    {
        "identifier": 'ACTION_476_turn_clockwise_45_degrees_n_times_8',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [2]
    },
    {
        "identifier": 'ACTION_476_pause_9',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'ACTION_476_end_loop_10',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_476_pause_11',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'ACTION_476_db_12',
        "command": 'db',
        "args": [0x3b, 0x00, 0x00, 0x05, 0xf2, 0x5b]
    },
    {
        "identifier": 'ACTION_476_walk_1_step_f_direction_13',
        "command": 'walk_1_step_f_direction'
    },
    {
        "identifier": 'ACTION_476_pause_14',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'ACTION_476_db_15',
        "command": 'db',
        "args": [0x3b, 0x00, 0x00, 0x05, 0xf2, 0x5b]
    },
    {
        "identifier": 'ACTION_476_jmp_16',
        "command": 'jmp',
        "args": ['ACTION_476_set_animation_speed_6']
    },
    {
        "identifier": 'ACTION_476_set_animation_speed_17',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_476_start_loop_n_times_18',
        "command": 'start_loop_n_times',
        "args": [1]
    },
    {
        "identifier": 'ACTION_476_face_mario_19',
        "command": 'face_mario'
    },
    {
        "identifier": 'ACTION_476_shift_f_direction_steps_20',
        "command": 'shift_f_direction_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_476_end_loop_21',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_476_jmp_22',
        "command": 'jmp',
        "args": ['ACTION_476_set_animation_speed_6']
    }
]
