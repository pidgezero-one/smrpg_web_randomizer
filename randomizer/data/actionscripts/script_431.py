from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_431_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_431_sequence_looping_on_1',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_431_reset_properties_2',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_431_set_object_memory_bits_3',
        "command": 'set_object_memory_bits',
        "args": [0x0e, [2, 3]]
    },
    {
        "identifier": 'ACTION_431_pause_4',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_431_jmp_5',
        "command": 'jmp',
        "args": ['ACTION_431_pause_4']
    }
]
