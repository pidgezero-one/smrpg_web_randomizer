from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_376_turn_random_direction_0',
        "command": 'turn_random_direction'
    },
    {
        "identifier": 'ACTION_376_pause_1',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'ACTION_376_turn_random_direction_2',
        "command": 'turn_random_direction'
    },
    {
        "identifier": 'ACTION_376_pause_3',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'ACTION_376_jmp_if_random_above_128_4',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_376_turn_random_direction_0']
    },
    {
        "identifier": 'ACTION_376_turn_random_direction_5',
        "command": 'turn_random_direction'
    },
    {
        "identifier": 'ACTION_376_pause_6',
        "command": 'pause',
        "args": [48]
    },
    {
        "identifier": 'ACTION_376_jmp_7',
        "command": 'jmp',
        "args": ['ACTION_376_turn_random_direction_0']
    }
]
