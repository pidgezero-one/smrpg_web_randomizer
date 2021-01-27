from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_128_set_object_memory_bits_0',
        "command": 'set_object_memory_bits',
        "args": [0x0b, [0, 1]]
    },
    {
        "identifier": 'ACTION_128_set_solidity_bits_1',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_128_jmp_if_random_above_66_2',
        "command": 'jmp_if_random_above_66',
        "args": [0x1c70, 'ACTION_128_pause_13']
    },
    {
        "identifier": 'ACTION_128_set_animation_speed_3',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_128_walk_1_step_southeast_4',
        "command": 'walk_1_step_southeast'
    },
    {
        "identifier": 'ACTION_128_set_animation_speed_5',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_128_turn_random_direction_6',
        "command": 'turn_random_direction'
    },
    {
        "identifier": 'ACTION_128_walk_1_step_f_direction_7',
        "command": 'walk_1_step_f_direction'
    },
    {
        "identifier": 'ACTION_128_jmp_if_random_above_128_8',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_128_set_animation_speed_14']
    },
    {
        "identifier": 'ACTION_128_walk_1_step_southeast_9',
        "command": 'walk_1_step_southeast'
    },
    {
        "identifier": 'ACTION_128_pause_10',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_128_jmp_if_random_above_128_11',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_128_set_animation_speed_14']
    },
    {
        "identifier": 'ACTION_128_walk_1_step_northeast_12',
        "command": 'walk_1_step_northeast'
    },
    {
        "identifier": 'ACTION_128_pause_13',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'ACTION_128_set_animation_speed_14',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_128_jmp_if_random_above_66_15',
        "command": 'jmp_if_random_above_66',
        "args": [0x1c97, 'ACTION_128_walk_1_step_northeast_12']
    },
    {
        "identifier": 'ACTION_128_walk_1_step_southwest_16',
        "command": 'walk_1_step_southwest'
    },
    {
        "identifier": 'ACTION_128_pause_17',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'ACTION_128_jmp_if_random_above_128_18',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_128_set_object_memory_bits_0']
    },
    {
        "identifier": 'ACTION_128_pause_19',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_128_jmp_if_random_above_66_20',
        "command": 'jmp_if_random_above_66',
        "args": [0x1c77, 'ACTION_128_pause_25']
    },
    {
        "identifier": 'ACTION_128_set_animation_speed_21',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_128_walk_1_step_northeast_22',
        "command": 'walk_1_step_northeast'
    },
    {
        "identifier": 'ACTION_128_walk_1_step_northwest_23',
        "command": 'walk_1_step_northwest'
    },
    {
        "identifier": 'ACTION_128_jmp_24',
        "command": 'jmp',
        "args": ['ACTION_128_set_animation_speed_14']
    },
    {
        "identifier": 'ACTION_128_pause_25',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'ACTION_128_set_animation_speed_26',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_128_shift_northeast_steps_27',
        "command": 'shift_northeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_128_jmp_28',
        "command": 'jmp',
        "args": ['ACTION_128_set_animation_speed_14']
    }
]
