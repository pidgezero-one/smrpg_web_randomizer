from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_29_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_29_sequence_looping_on_1',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_29_jmp_2',
        "command": 'jmp',
        "args": ['ACTION_98_set_animation_speed_0']
    }
]
