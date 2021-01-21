from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_818_visibility_on_0',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_818_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_818_play_sound_2',
        "command": 'play_sound',
        "args": [Sounds._030_SURPRISED_MONSTER, 4]
    },
    {
        "identifier": 'ACTION_818_jump_to_height_3',
        "command": 'jump_to_height',
        "args": [128]
    },
    {
        "identifier": 'ACTION_818_walk_1_step_f_direction_4',
        "command": 'walk_1_step_f_direction'
    },
    {
        "identifier": 'ACTION_818_set_solidity_bits_5',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_818_pause_6',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_818_db_7',
        "command": 'db',
        "args": [0xfd, 0x3d, 0x07, 0xc8, 0x9b]
    },
    {
        "identifier": 'ACTION_818_set_700C_to_pressed_button_8',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_818_jmp_if_var_not_equals_short_9',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x700c, 22, 'ACTION_818_set_solidity_bits_11']
    },
    {
        "identifier": 'ACTION_818_set_bit_10',
        "command": 'set_bit',
        "args": [0x7044, 7]
    },
    {
        "identifier": 'ACTION_818_set_solidity_bits_11',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_WALK_UNDER]]
    },
    {
        "identifier": 'ACTION_818_set_solidity_bits_12',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_818_set_priority_13',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_818_jmp_if_random_above_128_14',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_818_set_animation_speed_19']
    },
    {
        "identifier": 'ACTION_818_set_animation_speed_15',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_818_face_mario_16',
        "command": 'face_mario'
    },
    {
        "identifier": 'ACTION_818_walk_1_step_f_direction_17',
        "command": 'walk_1_step_f_direction'
    },
    {
        "identifier": 'ACTION_818_jmp_18',
        "command": 'jmp',
        "args": ['ACTION_818_jmp_if_random_above_128_14']
    },
    {
        "identifier": 'ACTION_818_set_animation_speed_19',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_818_turn_random_direction_20',
        "command": 'turn_random_direction'
    },
    {
        "identifier": 'ACTION_818_walk_1_step_f_direction_21',
        "command": 'walk_1_step_f_direction'
    },
    {
        "identifier": 'ACTION_818_jmp_22',
        "command": 'jmp',
        "args": ['ACTION_818_set_animation_speed_15']
    }
]
