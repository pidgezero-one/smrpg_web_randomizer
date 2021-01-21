from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_59_set_700C_to_current_level_0',
        "command": 'set_700C_to_current_level'
    },
    {
        "identifier": 'ACTION_59_jmp_if_var_equals_short_1',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 463, 'ACTION_59_set_700C_to_object_coord_23']
    },
    {
        "identifier": 'ACTION_59_jmp_if_var_equals_short_2',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 464, 'ACTION_59_set_700C_to_object_coord_23']
    },
    {
        "identifier": 'ACTION_59_jmp_if_var_equals_short_3',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 465, 'ACTION_59_set_700C_to_object_coord_23']
    },
    {
        "identifier": 'ACTION_59_jmp_if_var_equals_short_4',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 466, 'ACTION_59_set_700C_to_object_coord_23']
    },
    {
        "identifier": 'ACTION_59_jmp_if_var_equals_short_5',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 467, 'ACTION_59_set_700C_to_object_coord_23']
    },
    {
        "identifier": 'ACTION_59_jmp_if_var_equals_short_6',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 468, 'ACTION_59_set_700C_to_object_coord_23']
    },
    {
        "identifier": 'ACTION_59_object_memory_set_bit_7',
        "command": 'object_memory_set_bit',
        "args": [0x0b, [3]]
    },
    {
        "identifier": 'ACTION_59_set_object_memory_bits_8',
        "command": 'set_object_memory_bits',
        "args": [0x0b, bits=[0, 1]]
    },
    {
        "identifier": 'ACTION_59_face_southwest_9',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_59_set_animation_speed_10',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_59_shift_f_direction_steps_11',
        "command": 'shift_f_direction_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_59_pause_12',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'ACTION_59_shift_f_direction_steps_13',
        "command": 'shift_f_direction_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_59_pause_14',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'ACTION_59_shift_f_direction_steps_15',
        "command": 'shift_f_direction_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_59_pause_16',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'ACTION_59_shift_f_direction_steps_17',
        "command": 'shift_f_direction_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_59_pause_18',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'ACTION_59_jump_to_height_silent_19',
        "command": 'jump_to_height_silent',
        "args": [60]
    },
    {
        "identifier": 'ACTION_59_shift_f_direction_steps_20',
        "command": 'shift_f_direction_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_59_turn_random_direction_21',
        "command": 'turn_random_direction'
    },
    {
        "identifier": 'ACTION_59_jmp_22',
        "command": 'jmp',
        "args": ['ACTION_59_set_animation_speed_10']
    },
    {
        "identifier": 'ACTION_59_set_700C_to_object_coord_23',
        "command": 'set_700C_to_object_coord',
        "args": [AreaObjects.DUMMY_0X07, Coords.F]
    },
    {
        "identifier": 'ACTION_59_jmp_if_var_equals_short_24',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 1, 'ACTION_59_set_sprite_sequence_32']
    },
    {
        "identifier": 'ACTION_59_set_sprite_sequence_25',
        "command": 'set_sprite_sequence',
        "args": [21, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_59_pause_26',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_59_set_sprite_sequence_27',
        "command": 'set_sprite_sequence',
        "args": [22, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_59_pause_28',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_59_jmp_if_bit_clear_29',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 7, 'ACTION_59_set_700C_to_object_coord_23']
    },
    {
        "identifier": 'ACTION_59_set_sprite_sequence_30',
        "command": 'set_sprite_sequence',
        "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_59_ret_31',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_59_set_sprite_sequence_32',
        "command": 'set_sprite_sequence',
        "args": [21, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_59_pause_33',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_59_set_sprite_sequence_34',
        "command": 'set_sprite_sequence',
        "args": [22, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_59_pause_35',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_59_jmp_if_bit_clear_36',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 7, 'ACTION_59_set_700C_to_object_coord_23']
    },
    {
        "identifier": 'ACTION_59_set_sprite_sequence_37',
        "command": 'set_sprite_sequence',
        "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_59_ret_38',
        "command": 'ret'
    }
]
