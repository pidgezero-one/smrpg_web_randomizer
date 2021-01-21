from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_792_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_792_walk_1_step_north_1',
        "command": 'walk_1_step_north'
    },
    {
        "identifier": 'ACTION_792_walk_1_step_southwest_2',
        "command": 'walk_1_step_southwest'
    },
    {
        "identifier": 'ACTION_792_set_animation_speed_3',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_792_shift_northeast_steps_4',
        "command": 'shift_northeast_steps',
        "args": [11]
    },
    {
        "identifier": 'ACTION_792_ret_5',
        "command": 'ret'
    }
]
