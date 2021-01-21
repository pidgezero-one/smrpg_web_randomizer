from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_321_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_321_face_mario_1',
        "command": 'face_mario'
    },
    {
        "identifier": 'ACTION_321_pause_2',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_321_jmp_3',
        "command": 'jmp',
        "args": ['ACTION_321_face_mario_1']
    }
]
