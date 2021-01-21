from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_848_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_848_walk_1_step_southeast_1',
        "command": 'walk_1_step_southeast'
    },
    {
        "identifier": 'ACTION_848_shift_northeast_steps_2',
        "command": 'shift_northeast_steps',
        "args": [4]
    },
    {
        "identifier": 'ACTION_848_walk_1_step_northwest_3',
        "command": 'walk_1_step_northwest'
    },
    {
        "identifier": 'ACTION_848_shift_southwest_steps_4',
        "command": 'shift_southwest_steps',
        "args": [4]
    },
    {
        "identifier": 'ACTION_848_jmp_5',
        "command": 'jmp',
        "args": ['ACTION_848_set_animation_speed_0']
    }
]
