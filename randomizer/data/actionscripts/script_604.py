from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_604_set_priority_0',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_604_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_604_walk_1_step_southwest_2',
        "command": 'walk_1_step_southwest'
    },
    {
        "identifier": 'ACTION_604_walk_1_step_northwest_3',
        "command": 'walk_1_step_northwest'
    },
    {
        "identifier": 'ACTION_604_pause_4',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'ACTION_604_set_animation_speed_5',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_604_walk_1_step_east_6',
        "command": 'walk_1_step_east'
    },
    {
        "identifier": 'ACTION_604_pause_7',
        "command": 'pause',
        "args": [13]
    },
    {
        "identifier": 'ACTION_604_jmp_8',
        "command": 'jmp',
        "args": ['ACTION_604_set_priority_0']
    }
]
