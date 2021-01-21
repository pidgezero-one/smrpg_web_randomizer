from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_346_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_346_walk_1_step_southeast_1',
        "command": 'walk_1_step_southeast'
    },
    {
        "identifier": 'ACTION_346_shift_northwest_steps_2',
        "command": 'shift_northwest_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_346_shift_southeast_steps_3',
        "command": 'shift_southeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_346_jmp_4',
        "command": 'jmp',
        "args": ['ACTION_346_set_animation_speed_0']
    }
]
