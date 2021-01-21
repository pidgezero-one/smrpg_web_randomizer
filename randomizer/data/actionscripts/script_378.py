from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_378_sequence_looping_on_0',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_378_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_378_pause_2',
        "command": 'pause',
        "args": [120]
    },
    {
        "identifier": 'ACTION_378_face_southwest_3',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_378_set_bit_4',
        "command": 'set_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'ACTION_378_pause_5',
        "command": 'pause',
        "args": [120]
    },
    {
        "identifier": 'ACTION_378_clear_bit_6',
        "command": 'clear_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'ACTION_378_face_southeast_7',
        "command": 'face_southeast'
    },
    {
        "identifier": 'ACTION_378_jmp_if_random_above_128_8',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_378_sequence_looping_on_0']
    },
    {
        "identifier": 'ACTION_378_pause_9',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'ACTION_378_jmp_10',
        "command": 'jmp',
        "args": ['ACTION_378_sequence_looping_on_0']
    }
]
