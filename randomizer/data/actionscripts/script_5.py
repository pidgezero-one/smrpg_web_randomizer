from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_5_turn_random_direction_0',
        "command": 'turn_random_direction'
    },
    {
        "identifier": 'ACTION_5_walk_1_step_f_direction_1',
        "command": 'walk_1_step_f_direction'
    },
    {
        "identifier": 'ACTION_5_pause_2',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_5_jmp_if_random_above_128_3',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_5_pause_2']
    },
    {
        "identifier": 'ACTION_5_jmp_if_random_above_128_4',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_5_walk_1_step_f_direction_1']
    },
    {
        "identifier": 'ACTION_5_jmp_if_random_above_66_5',
        "command": 'jmp_if_random_above_66',
        "args": [0x083d, 'ACTION_5_set_animation_speed_10']
    },
    {
        "identifier": 'ACTION_5_set_animation_speed_6',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_5_jmp_7',
        "command": 'jmp',
        "args": ['ACTION_5_turn_random_direction_0']
    },
    {
        "identifier": 'ACTION_5_set_animation_speed_8',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_5_jmp_9',
        "command": 'jmp',
        "args": ['ACTION_5_turn_random_direction_0']
    },
    {
        "identifier": 'ACTION_5_set_animation_speed_10',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_5_jmp_11',
        "command": 'jmp',
        "args": ['ACTION_5_turn_random_direction_0']
    }
]
