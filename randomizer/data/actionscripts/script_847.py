from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_847_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_847_shift_northwest_steps_1',
        "command": 'shift_northwest_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_847_walk_1_step_southwest_2',
        "command": 'walk_1_step_southwest'
    },
    {
        "identifier": 'ACTION_847_walk_1_step_southeast_3',
        "command": 'walk_1_step_southeast'
    },
    {
        "identifier": 'ACTION_847_walk_1_step_northeast_4',
        "command": 'walk_1_step_northeast'
    },
    {
        "identifier": 'ACTION_847_shift_southeast_steps_5',
        "command": 'shift_southeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_847_jmp_6',
        "command": 'jmp',
        "args": ['ACTION_847_set_animation_speed_0']
    }
]
