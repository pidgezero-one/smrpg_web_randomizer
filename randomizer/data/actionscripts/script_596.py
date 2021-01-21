from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_596_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_596_shift_southwest_steps_1',
        "command": 'shift_southwest_steps',
        "args": [11]
    },
    {
        "identifier": 'ACTION_596_set_bit_2',
        "command": 'set_bit',
        "args": [0x7044, 5]
    },
    {
        "identifier": 'ACTION_596_shift_southwest_steps_3',
        "command": 'shift_southwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_596_clear_bit_4',
        "command": 'clear_bit',
        "args": [0x7044, 5]
    },
    {
        "identifier": 'ACTION_596_set_bit_5',
        "command": 'set_bit',
        "args": [0x7044, 7]
    },
    {
        "identifier": 'ACTION_596_pause_6',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_596_walk_1_step_southeast_7',
        "command": 'walk_1_step_southeast'
    },
    {
        "identifier": 'ACTION_596_walk_1_step_southeast_8',
        "command": 'walk_1_step_southeast'
    },
    {
        "identifier": 'ACTION_596_walk_1_step_southwest_9',
        "command": 'walk_1_step_southwest'
    },
    {
        "identifier": 'ACTION_596_jmp_10',
        "command": 'jmp',
        "args": ['ACTION_596_walk_1_step_southwest_9']
    }
]
