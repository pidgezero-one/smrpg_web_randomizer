from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_514_sequence_looping_on_0',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_514_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_514_face_mario_2',
        "command": 'face_mario'
    },
    {
        "identifier": 'ACTION_514_jmp_3',
        "command": 'jmp',
        "args": ['ACTION_514_sequence_looping_on_0']
    },
    {
        "identifier": 'ACTION_514_ret_4',
        "command": 'ret'
    }
]