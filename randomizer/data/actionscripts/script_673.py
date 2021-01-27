from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_673_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_673_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_673_jmp_if_random_above_128_2',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_673_walk_1_step_northeast_5']
    },
    {
        "identifier": 'ACTION_673_walk_1_step_southwest_3',
        "command": 'walk_1_step_southwest'
    },
    {
        "identifier": 'ACTION_673_set_animation_speed_4',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_673_walk_1_step_northeast_5',
        "command": 'walk_1_step_northeast'
    },
    {
        "identifier": 'ACTION_673_jmp_if_random_above_128_6',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_673_walk_1_step_southwest_9']
    },
    {
        "identifier": 'ACTION_673_walk_1_step_northeast_7',
        "command": 'walk_1_step_northeast'
    },
    {
        "identifier": 'ACTION_673_set_animation_speed_8',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_673_walk_1_step_southwest_9',
        "command": 'walk_1_step_southwest'
    },
    {
        "identifier": 'ACTION_673_set_animation_speed_10',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_673_jmp_if_random_above_66_11',
        "command": 'jmp_if_random_above_66',
        "args": [0x7baf, 'ACTION_673_jmp_if_random_above_128_2']
    },
    {
        "identifier": 'ACTION_673_jmp_12',
        "command": 'jmp',
        "args": ['ACTION_673_walk_1_step_northeast_5']
    }
]
