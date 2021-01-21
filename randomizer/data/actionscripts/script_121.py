from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_121_turn_random_direction_0',
        "command": 'turn_random_direction'
    },
    {
        "identifier": 'ACTION_121_pause_1',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'ACTION_121_turn_random_direction_2',
        "command": 'turn_random_direction'
    },
    {
        "identifier": 'ACTION_121_pause_3',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_121_jmp_4',
        "command": 'jmp',
        "args": ['ACTION_121_turn_random_direction_0']
    }
]
