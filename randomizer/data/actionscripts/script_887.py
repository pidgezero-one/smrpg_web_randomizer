from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_887_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_887_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_887_shift_southeast_steps_2',
        "command": 'shift_southeast_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_887_jmp_if_random_above_128_3',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_887_walk_1_step_southwest_5']
    },
    {
        "identifier": 'ACTION_887_pause_4',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'ACTION_887_walk_1_step_southwest_5',
        "command": 'walk_1_step_southwest'
    },
    {
        "identifier": 'ACTION_887_jmp_if_random_above_128_6',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_887_shift_northwest_steps_8']
    },
    {
        "identifier": 'ACTION_887_pause_7',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_887_shift_northwest_steps_8',
        "command": 'shift_northwest_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_887_jmp_if_random_above_128_9',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_887_walk_1_step_northeast_11']
    },
    {
        "identifier": 'ACTION_887_pause_10',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_887_walk_1_step_northeast_11',
        "command": 'walk_1_step_northeast'
    },
    {
        "identifier": 'ACTION_887_jmp_12',
        "command": 'jmp',
        "args": ['ACTION_887_set_animation_speed_0']
    }
]
