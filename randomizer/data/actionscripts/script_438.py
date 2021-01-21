from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_438_object_memory_set_bit_0',
        "command": 'object_memory_set_bit',
        "args": [0x0d, [6]]
    },
    {
        "identifier": 'ACTION_438_set_priority_1',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_438_db_2',
        "command": 'db',
        "args": [0x20, 0x07]
    },
    {
        "identifier": 'ACTION_438_embedded_animation_routine_3',
        "command": 'embedded_animation_routine',
        "args": [0x26]
    },
    {
        "identifier": 'ACTION_438_embedded_animation_routine_4',
        "command": 'embedded_animation_routine',
        "args": [0x27]
    },
    {
        "identifier": 'ACTION_438_embedded_animation_routine_5',
        "command": 'embedded_animation_routine',
        "args": [0x28]
    },
    {
        "identifier": 'ACTION_438_pause_6',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_438_jmp_7',
        "command": 'jmp',
        "args": ['ACTION_438_pause_6']
    }
]
