from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_935_set_solidity_bits_0',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_935_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_935_clear_solidity_bits_2',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_935_shift_z_up_steps_3',
        "command": 'shift_z_up_steps',
        "args": [8]
    },
    {
        "identifier": 'ACTION_935_object_memory_set_bit_4',
        "command": 'object_memory_set_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_935_floating_off_5',
        "command": 'floating_off'
    },
    {
        "identifier": 'ACTION_935_set_random_6',
        "command": 'set_random',
        "args": [0x700c, 8]
    },
    {
        "identifier": 'ACTION_935_face_east_7',
        "command": 'face_east'
    },
    {
        "identifier": 'ACTION_935_shift_f_direction_steps_8',
        "command": 'shift_f_direction_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_935_jmp_if_random_above_128_9',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_935_set_random_6']
    },
    {
        "identifier": 'ACTION_935_jmp_if_random_above_128_10',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_935_set_random_6']
    },
    {
        "identifier": 'ACTION_935_visibility_on_11',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_935_object_memory_clear_bit_12',
        "command": 'object_memory_clear_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_935_floating_on_13',
        "command": 'floating_on'
    },
    {
        "identifier": 'ACTION_935_set_bit_14',
        "command": 'set_bit',
        "args": [0x7043, 2]
    },
    {
        "identifier": 'ACTION_935_set_solidity_bits_15',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_935_set_animation_speed_16',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_935_jump_to_height_silent_17',
        "command": 'jump_to_height_silent',
        "args": [0]
    },
    {
        "identifier": 'ACTION_935_pause_18',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_935_db_19',
        "command": 'db',
        "args": [0xfd, 0x3d, 0x07, 0x2e, 0xad]
    },
    {
        "identifier": 'ACTION_935_set_animation_speed_20',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_935_set_animation_speed_21',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_935_walk_1_step_f_direction_22',
        "command": 'walk_1_step_f_direction'
    },
    {
        "identifier": 'ACTION_935_jump_to_height_silent_23',
        "command": 'jump_to_height_silent',
        "args": [0]
    },
    {
        "identifier": 'ACTION_935_turn_random_direction_24',
        "command": 'turn_random_direction'
    },
    {
        "identifier": 'ACTION_935_walk_1_step_f_direction_25',
        "command": 'walk_1_step_f_direction'
    },
    {
        "identifier": 'ACTION_935_jmp_if_random_above_128_26',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_935_set_animation_speed_20']
    },
    {
        "identifier": 'ACTION_935_face_mario_27',
        "command": 'face_mario'
    },
    {
        "identifier": 'ACTION_935_set_animation_speed_28',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_935_set_animation_speed_29',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_935_walk_1_step_f_direction_30',
        "command": 'walk_1_step_f_direction'
    },
    {
        "identifier": 'ACTION_935_jmp_31',
        "command": 'jmp',
        "args": ['ACTION_935_set_animation_speed_20']
    }
]
