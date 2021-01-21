from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_272_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_272_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_272_set_700C_to_object_coord_2',
        "command": 'set_700C_to_object_coord',
        "args": [AreaObjects.DUMMY_0X07, Coords.F]
    },
    {
        "identifier": 'ACTION_272_jmp_if_var_equals_short_3',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 7, 'ACTION_272_set_sprite_sequence_30']
    },
    {
        "identifier": 'ACTION_272_jmp_if_var_equals_short_4',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 1, 'ACTION_272_set_sprite_sequence_30']
    },
    {
        "identifier": 'ACTION_272_set_sprite_sequence_5',
        "command": 'set_sprite_sequence',
        "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_272_object_memory_set_bit_6',
        "command": 'object_memory_set_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_272_clear_solidity_bits_7',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_272_set_700C_to_pressed_button_8',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_272_mem_700C_and_const_9',
        "command": 'mem_700C_and_const',
        "args": [0x0003]
    },
    {
        "identifier": 'ACTION_272_mem_700C_shift_left_10',
        "command": 'mem_700C_shift_left',
        "args": [0x7018, 255]
    },
    {
        "identifier": 'ACTION_272_load_mem_11',
        "command": 'load_mem',
        "args": [0x700c]
    },
    {
        "identifier": 'ACTION_272_pause_12',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_272_end_loop_13',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_272_pause_14',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'ACTION_272_db_15',
        "command": 'db',
        "args": [0x3b, 0x00, 0x80, 0x01, 0x5b, 0x31]
    },
    {
        "identifier": 'ACTION_272_jmp_16',
        "command": 'jmp',
        "args": ['ACTION_272_pause_14']
    },
    {
        "identifier": 'ACTION_272_play_sound_17',
        "command": 'play_sound',
        "args": [Sounds._117_SPINNING_MONSTER, 4]
    },
    {
        "identifier": 'ACTION_272_set_sprite_sequence_18',
        "command": 'set_sprite_sequence',
        "args": [8, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF]]
    },
    {
        "identifier": 'ACTION_272_pause_19',
        "command": 'pause',
        "args": [18]
    },
    {
        "identifier": 'ACTION_272_object_memory_clear_bit_20',
        "command": 'object_memory_clear_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_272_set_solidity_bits_21',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_272_start_loop_n_times_22',
        "command": 'start_loop_n_times',
        "args": [1]
    },
    {
        "identifier": 'ACTION_272_face_mario_23',
        "command": 'face_mario'
    },
    {
        "identifier": 'ACTION_272_shift_f_direction_steps_24',
        "command": 'shift_f_direction_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_272_end_loop_25',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_272_db_26',
        "command": 'db',
        "args": [0x3b, 0x00, 0x00, 0x03, 0x67, 0x31]
    },
    {
        "identifier": 'ACTION_272_pause_27',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_272_jmp_if_random_above_128_28',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_272_start_loop_n_times_22']
    },
    {
        "identifier": 'ACTION_272_jmp_29',
        "command": 'jmp',
        "args": ['ACTION_272_set_animation_speed_0']
    },
    {
        "identifier": 'ACTION_272_set_sprite_sequence_30',
        "command": 'set_sprite_sequence',
        "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_272_object_memory_set_bit_31',
        "command": 'object_memory_set_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_272_clear_solidity_bits_32',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_272_set_700C_to_pressed_button_33',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_272_mem_700C_and_const_34',
        "command": 'mem_700C_and_const',
        "args": [0x0003]
    },
    {
        "identifier": 'ACTION_272_mem_700C_shift_left_35',
        "command": 'mem_700C_shift_left',
        "args": [0x7018, 255]
    },
    {
        "identifier": 'ACTION_272_load_mem_36',
        "command": 'load_mem',
        "args": [0x700c]
    },
    {
        "identifier": 'ACTION_272_pause_37',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_272_end_loop_38',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_272_pause_39',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'ACTION_272_db_40',
        "command": 'db',
        "args": [0x3b, 0x00, 0x00, 0x03, 0x9b, 0x31]
    },
    {
        "identifier": 'ACTION_272_jmp_41',
        "command": 'jmp',
        "args": ['ACTION_272_pause_39']
    },
    {
        "identifier": 'ACTION_272_play_sound_42',
        "command": 'play_sound',
        "args": [Sounds._117_SPINNING_MONSTER, 4]
    },
    {
        "identifier": 'ACTION_272_set_sprite_sequence_43',
        "command": 'set_sprite_sequence',
        "args": [8, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF]]
    },
    {
        "identifier": 'ACTION_272_pause_44',
        "command": 'pause',
        "args": [18]
    },
    {
        "identifier": 'ACTION_272_object_memory_clear_bit_45',
        "command": 'object_memory_clear_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_272_set_solidity_bits_46',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_272_jmp_47',
        "command": 'jmp',
        "args": ['ACTION_272_start_loop_n_times_22']
    }
]
