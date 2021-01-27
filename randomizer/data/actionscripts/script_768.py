from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_768_set_700C_to_current_level_0',
        "command": 'set_700C_to_current_level'
    },
    {
        "identifier": 'ACTION_768_jmp_if_700C_equals_short_1',
        "command": 'jmp_if_700C_equals_short',
        "args": [262, 'ACTION_768_set_priority_21']
    },
    {
        "identifier": 'ACTION_768_jmp_if_700C_equals_short_2',
        "command": 'jmp_if_700C_equals_short',
        "args": [270, 'ACTION_768_set_priority_21']
    },
    {
        "identifier": 'ACTION_768_set_700C_to_pressed_button_3',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_768_add_4',
        "command": 'add',
        "args": [0x700c, 65517]
    },
    {
        "identifier": 'ACTION_768_load_mem_5',
        "command": 'load_mem',
        "args": [0x700c]
    },
    {
        "identifier": 'ACTION_768_pause_6',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'ACTION_768_end_loop_7',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_768_sequence_looping_on_8',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_768_set_animation_speed_9',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_768_set_animation_speed_10',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_768_turn_clockwise_45_degrees_11',
        "command": 'turn_clockwise_45_degrees'
    },
    {
        "identifier": 'ACTION_768_walk_1_step_f_direction_12',
        "command": 'walk_1_step_f_direction'
    },
    {
        "identifier": 'ACTION_768_set_animation_speed_13',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_768_pause_14',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'ACTION_768_set_animation_speed_15',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_768_turn_random_direction_16',
        "command": 'turn_random_direction'
    },
    {
        "identifier": 'ACTION_768_walk_1_step_f_direction_17',
        "command": 'walk_1_step_f_direction'
    },
    {
        "identifier": 'ACTION_768_set_animation_speed_18',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_768_pause_19',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_768_jmp_20',
        "command": 'jmp',
        "args": ['ACTION_768_set_animation_speed_10']
    },
    {
        "identifier": 'ACTION_768_set_priority_21',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_768_sequence_looping_on_22',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_768_set_700C_to_pressed_button_23',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_768_add_24',
        "command": 'add',
        "args": [0x700c, 65517]
    },
    {
        "identifier": 'ACTION_768_load_mem_25',
        "command": 'load_mem',
        "args": [0x700c]
    },
    {
        "identifier": 'ACTION_768_pause_26',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_768_end_loop_27',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_768_face_mario_28',
        "command": 'face_mario'
    },
    {
        "identifier": 'ACTION_768_set_animation_speed_29',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_768_pause_30',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'ACTION_768_face_mario_31',
        "command": 'face_mario'
    },
    {
        "identifier": 'ACTION_768_set_animation_speed_32',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_768_pause_33',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'ACTION_768_jmp_34',
        "command": 'jmp',
        "args": ['ACTION_768_face_mario_28']
    }
]
