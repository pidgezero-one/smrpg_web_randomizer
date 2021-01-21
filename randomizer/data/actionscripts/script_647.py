from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_647_pause_0',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_647_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_647_shift_east_steps_2',
        "command": 'shift_east_steps',
        "args": [7]
    },
    {
        "identifier": 'ACTION_647_set_animation_speed_3',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_647_shift_east_steps_4',
        "command": 'shift_east_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_647_set_animation_speed_5',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_647_walk_1_step_east_6',
        "command": 'walk_1_step_east'
    },
    {
        "identifier": 'ACTION_647_set_animation_speed_7',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_647_ret_8',
        "command": 'ret'
    }
]
