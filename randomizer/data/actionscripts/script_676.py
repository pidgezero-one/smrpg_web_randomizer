from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_676_set_object_memory_bits_0',
        "command": 'set_object_memory_bits',
        "args": [0x0b, [1]]
    },
    {
        "identifier": 'ACTION_676_set_solidity_bits_1',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_676_set_solidity_bits_2',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.BIT_4]]
    },
    {
        "identifier": 'ACTION_676_set_short_3',
        "command": 'set_short',
        "args": [0x702c, 0x0004]
    },
    {
        "identifier": 'ACTION_676_set_short_4',
        "command": 'set_short',
        "args": [0x7030, 0x0014]
    },
    {
        "identifier": 'ACTION_676_set_animation_speed_5',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_676_set_animation_speed_6',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_676_walk_1_step_northeast_7',
        "command": 'walk_1_step_northeast'
    },
    {
        "identifier": 'ACTION_676_jump_to_subroutine_8',
        "command": 'jump_to_subroutine',
        "args": [0x7c49]
    },
    {
        "identifier": 'ACTION_676_jmp_if_var_equals_short_9',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7030, 0, 'ACTION_676_set_animation_speed_21']
    },
    {
        "identifier": 'ACTION_676_jmp_if_random_above_66_10',
        "command": 'jmp_if_random_above_66',
        "args": [0x7c05, 'ACTION_676_jmp_if_var_equals_short_12']
    },
    {
        "identifier": 'ACTION_676_jmp_11',
        "command": 'jmp',
        "args": ['ACTION_676_set_animation_speed_5']
    },
    {
        "identifier": 'ACTION_676_jmp_if_var_equals_short_12',
        "command": 'jmp_if_var_equals_short',
        "args": [0x702c, 0, 'ACTION_676_set_animation_speed_5']
    },
    {
        "identifier": 'ACTION_676_set_animation_speed_13',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_676_set_animation_speed_14',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_676_walk_1_step_northeast_15',
        "command": 'walk_1_step_northeast'
    },
    {
        "identifier": 'ACTION_676_jump_to_subroutine_16',
        "command": 'jump_to_subroutine',
        "args": [0x7c49]
    },
    {
        "identifier": 'ACTION_676_jmp_if_var_equals_short_17',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7030, 0, 'ACTION_676_set_animation_speed_21']
    },
    {
        "identifier": 'ACTION_676_jump_to_subroutine_18',
        "command": 'jump_to_subroutine',
        "args": [0x7c4c]
    },
    {
        "identifier": 'ACTION_676_jmp_if_random_above_66_19',
        "command": 'jmp_if_random_above_66',
        "args": [0x7c1b, 'ACTION_676_set_animation_speed_5']
    },
    {
        "identifier": 'ACTION_676_jmp_20',
        "command": 'jmp',
        "args": ['ACTION_676_jmp_if_var_equals_short_12']
    },
    {
        "identifier": 'ACTION_676_set_animation_speed_21',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_676_face_southwest_22',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_676_pause_23',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'ACTION_676_set_animation_speed_24',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_676_shift_southwest_steps_25',
        "command": 'shift_southwest_steps',
        "args": [20]
    },
    {
        "identifier": 'ACTION_676_face_northeast_26',
        "command": 'face_northeast'
    },
    {
        "identifier": 'ACTION_676_pause_27',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'ACTION_676_jmp_28',
        "command": 'jmp',
        "args": ['ACTION_676_set_object_memory_bits_0']
    },
    {
        "identifier": 'ACTION_676_dec_short_29',
        "command": 'dec_short',
        "args": [0x7030]
    },
    {
        "identifier": 'ACTION_676_ret_30',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_676_dec_short_31',
        "command": 'dec_short',
        "args": [0x702c]
    },
    {
        "identifier": 'ACTION_676_ret_32',
        "command": 'ret'
    }
]
