from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_472_visibility_off_0',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_472_db_1',
        "command": 'db',
        "args": [0xfd, 0x12]
    },
    {
        "identifier": 'ACTION_472_face_northeast_2',
        "command": 'face_northeast'
    },
    {
        "identifier": 'ACTION_472_set_700C_to_pressed_button_3',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_472_add_4',
        "command": 'add',
        "args": [0x700c, 65512]
    },
    {
        "identifier": 'ACTION_472_load_mem_5',
        "command": 'load_mem',
        "args": [0x700c]
    },
    {
        "identifier": 'ACTION_472_pause_6',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_472_end_loop_7',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_472_pause_8',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'ACTION_472_db_9',
        "command": 'db',
        "args": [0x3b, 0x00, 0x80, 0x03, 0x17, 0x5b]
    },
    {
        "identifier": 'ACTION_472_jmp_10',
        "command": 'jmp',
        "args": ['ACTION_472_pause_8']
    },
    {
        "identifier": 'ACTION_472_db_11',
        "command": 'db',
        "args": [0x3c, 0x00, 0x40, 0x1f, 0x5b]
    },
    {
        "identifier": 'ACTION_472_jmp_12',
        "command": 'jmp',
        "args": ['ACTION_472_pause_8']
    },
    {
        "identifier": 'ACTION_472_visibility_on_13',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_472_sequence_looping_on_14',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_472_set_solidity_bits_15',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.BIT_4]]
    },
    {
        "identifier": 'ACTION_472_set_solidity_bits_16',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_472_object_memory_clear_bit_17',
        "command": 'object_memory_clear_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_472_play_sound_18',
        "command": 'play_sound',
        "args": [Sounds._030_SURPRISED_MONSTER, 4]
    },
    {
        "identifier": 'ACTION_472_set_animation_speed_19',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FASTER, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_472_jump_to_height_20',
        "command": 'jump_to_height',
        "args": [108]
    },
    {
        "identifier": 'ACTION_472_shift_northeast_steps_21',
        "command": 'shift_northeast_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_472_pause_22',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'ACTION_472_face_northwest_23',
        "command": 'face_northwest'
    },
    {
        "identifier": 'ACTION_472_set_animation_speed_24',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_472_set_animation_speed_25',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_472_walk_1_step_f_direction_26',
        "command": 'walk_1_step_f_direction'
    },
    {
        "identifier": 'ACTION_472_pause_27',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'ACTION_472_turn_clockwise_45_degrees_n_times_28',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [6]
    },
    {
        "identifier": 'ACTION_472_pause_29',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'ACTION_472_turn_clockwise_45_degrees_n_times_30',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [6]
    },
    {
        "identifier": 'ACTION_472_pause_31',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'ACTION_472_jmp_32',
        "command": 'jmp',
        "args": ['ACTION_472_walk_1_step_f_direction_26']
    }
]
