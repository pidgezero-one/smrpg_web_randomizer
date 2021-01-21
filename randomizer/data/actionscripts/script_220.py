from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_220_face_west_0',
        "command": 'face_west'
    },
    {
        "identifier": 'ACTION_220_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_220_sequence_looping_on_2',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_220_set_short_3',
        "command": 'set_short',
        "args": [0x703e, 0x0004]
    },
    {
        "identifier": 'ACTION_220_ret_4',
        "command": 'ret'
    }
]
