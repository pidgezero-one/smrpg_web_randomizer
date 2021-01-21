from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_169_sequence_looping_on_0',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_169_set_700C_to_pressed_button_1',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_169_add_2',
        "command": 'add',
        "args": [0x700c, 65517]
    },
    {
        "identifier": 'ACTION_169_load_mem_3',
        "command": 'load_mem',
        "args": [0x700c]
    },
    {
        "identifier": 'ACTION_169_pause_4',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_169_end_loop_5',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_169_set_animation_speed_6',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_169_set_animation_speed_7',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_169_set_sprite_sequence_8',
        "command": 'set_sprite_sequence',
        "args": [3, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_169_walk_1_step_southwest_9',
        "command": 'walk_1_step_southwest'
    },
    {
        "identifier": 'ACTION_169_pause_10',
        "command": 'pause',
        "args": [9]
    },
    {
        "identifier": 'ACTION_169_reset_properties_11',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_169_pause_12',
        "command": 'pause',
        "args": [9]
    },
    {
        "identifier": 'ACTION_169_db_13',
        "command": 'db',
        "args": [0x3b, 0x00, 0x00, 0x06, 0x43, 0x21]
    },
    {
        "identifier": 'ACTION_169_start_loop_n_times_14',
        "command": 'start_loop_n_times',
        "args": [2]
    },
    {
        "identifier": 'ACTION_169_turn_clockwise_45_degrees_n_times_15',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [6]
    },
    {
        "identifier": 'ACTION_169_walk_1_step_f_direction_16',
        "command": 'walk_1_step_f_direction'
    },
    {
        "identifier": 'ACTION_169_db_17',
        "command": 'db',
        "args": [0x3b, 0x00, 0x00, 0x06, 0x43, 0x21]
    },
    {
        "identifier": 'ACTION_169_end_loop_18',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_169_pause_19',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'ACTION_169_face_southeast_20',
        "command": 'face_southeast'
    },
    {
        "identifier": 'ACTION_169_pause_21',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'ACTION_169_db_22',
        "command": 'db',
        "args": [0x3b, 0x00, 0x00, 0x06, 0x43, 0x21]
    },
    {
        "identifier": 'ACTION_169_set_sprite_sequence_23',
        "command": 'set_sprite_sequence',
        "args": [3, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_169_walk_1_step_southeast_24',
        "command": 'walk_1_step_southeast'
    },
    {
        "identifier": 'ACTION_169_pause_25',
        "command": 'pause',
        "args": [9]
    },
    {
        "identifier": 'ACTION_169_reset_properties_26',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_169_pause_27',
        "command": 'pause',
        "args": [9]
    },
    {
        "identifier": 'ACTION_169_db_28',
        "command": 'db',
        "args": [0x3b, 0x00, 0x00, 0x06, 0x43, 0x21]
    },
    {
        "identifier": 'ACTION_169_start_loop_n_times_29',
        "command": 'start_loop_n_times',
        "args": [2]
    },
    {
        "identifier": 'ACTION_169_turn_clockwise_45_degrees_n_times_30',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [2]
    },
    {
        "identifier": 'ACTION_169_walk_1_step_f_direction_31',
        "command": 'walk_1_step_f_direction'
    },
    {
        "identifier": 'ACTION_169_db_32',
        "command": 'db',
        "args": [0x3b, 0x00, 0x00, 0x06, 0x43, 0x21]
    },
    {
        "identifier": 'ACTION_169_end_loop_33',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_169_pause_34',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'ACTION_169_face_southwest_35',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_169_pause_36',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'ACTION_169_db_37',
        "command": 'db',
        "args": [0x3b, 0x00, 0x00, 0x06, 0x43, 0x21]
    },
    {
        "identifier": 'ACTION_169_jmp_38',
        "command": 'jmp',
        "args": ['ACTION_169_set_animation_speed_6']
    },
    {
        "identifier": 'ACTION_169_set_animation_speed_39',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_169_set_animation_speed_40',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_169_start_loop_n_times_41',
        "command": 'start_loop_n_times',
        "args": [1]
    },
    {
        "identifier": 'ACTION_169_face_mario_42',
        "command": 'face_mario'
    },
    {
        "identifier": 'ACTION_169_shift_f_direction_steps_43',
        "command": 'shift_f_direction_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_169_end_loop_44',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_169_jmp_45',
        "command": 'jmp',
        "args": ['ACTION_169_set_animation_speed_6']
    }
]
