from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_986_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_986_shift_northwest_steps_1',
        "command": 'shift_northwest_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_986_pause_2',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'ACTION_986_shift_southeast_steps_3',
        "command": 'shift_southeast_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_986_pause_4',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_986_jmp_5',
        "command": 'jmp',
        "args": ['ACTION_986_set_animation_speed_0']
    }
]
