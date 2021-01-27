from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_714_set_700C_to_current_level_0',
        "command": 'set_700C_to_current_level'
    },
    {
        "identifier": 'ACTION_714_jmp_if_700C_equals_short_1',
        "command": 'jmp_if_700C_equals_short',
        "args": [457, 'ACTION_714_set_animation_speed_19']
    },
    {
        "identifier": 'ACTION_714_set_priority_2',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_714_sequence_looping_on_3',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_714_shadow_on_4',
        "command": 'shadow_on'
    },
    {
        "identifier": 'ACTION_714_set_animation_speed_5',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_714_set_animation_speed_6',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_714_set_700C_to_pressed_button_7',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_714_add_8',
        "command": 'add',
        "args": [0x700c, 65517]
    },
    {
        "identifier": 'ACTION_714_load_mem_9',
        "command": 'load_mem',
        "args": [0x700c]
    },
    {
        "identifier": 'ACTION_714_pause_10',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_714_end_loop_11',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_714_turn_clockwise_45_degrees_12',
        "command": 'turn_clockwise_45_degrees'
    },
    {
        "identifier": 'ACTION_714_shift_f_direction_steps_13',
        "command": 'shift_f_direction_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_714_turn_random_direction_14',
        "command": 'turn_random_direction'
    },
    {
        "identifier": 'ACTION_714_shift_f_direction_steps_15',
        "command": 'shift_f_direction_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_714_face_mario_16',
        "command": 'face_mario'
    },
    {
        "identifier": 'ACTION_714_walk_1_step_f_direction_17',
        "command": 'walk_1_step_f_direction'
    },
    {
        "identifier": 'ACTION_714_jmp_18',
        "command": 'jmp',
        "args": ['ACTION_714_turn_clockwise_45_degrees_12']
    },
    {
        "identifier": 'ACTION_714_set_animation_speed_19',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_714_set_animation_speed_20',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_714_face_mario_21',
        "command": 'face_mario'
    },
    {
        "identifier": 'ACTION_714_shift_f_direction_steps_22',
        "command": 'shift_f_direction_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_714_turn_random_direction_23',
        "command": 'turn_random_direction'
    },
    {
        "identifier": 'ACTION_714_walk_1_step_f_direction_24',
        "command": 'walk_1_step_f_direction'
    },
    {
        "identifier": 'ACTION_714_turn_clockwise_45_degrees_25',
        "command": 'turn_clockwise_45_degrees'
    },
    {
        "identifier": 'ACTION_714_walk_1_step_f_direction_26',
        "command": 'walk_1_step_f_direction'
    },
    {
        "identifier": 'ACTION_714_jmp_27',
        "command": 'jmp',
        "args": ['ACTION_714_face_mario_21']
    }
]
