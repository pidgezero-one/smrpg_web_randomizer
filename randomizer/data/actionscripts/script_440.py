from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_440_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_440_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_440_walk_1_step_f_direction_2',
        "command": 'walk_1_step_f_direction'
    },
    {
        "identifier": 'ACTION_440_turn_random_direction_3',
        "command": 'turn_random_direction'
    },
    {
        "identifier": 'ACTION_440_jmp_4',
        "command": 'jmp',
        "args": ['ACTION_440_set_animation_speed_0']
    }
]
