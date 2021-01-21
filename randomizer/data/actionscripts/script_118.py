from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_118_jmp_if_random_above_128_0',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_118_set_animation_speed_2']
    },
    {
        "identifier": 'ACTION_118_pause_1',
        "command": 'pause',
        "args": [28]
    },
    {
        "identifier": 'ACTION_118_set_animation_speed_2',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_118_sequence_looping_on_3',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_118_ret_4',
        "command": 'ret'
    }
]
