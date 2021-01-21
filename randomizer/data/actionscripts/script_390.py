from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_390_reset_properties_0',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_390_face_northeast_1',
        "command": 'face_northeast'
    },
    {
        "identifier": 'ACTION_390_set_animation_speed_2',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_390_sequence_looping_on_3',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_390_pause_4',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'ACTION_390_sequence_looping_off_5',
        "command": 'sequence_looping_off'
    },
    {
        "identifier": 'ACTION_390_set_animation_speed_6',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_390_pause_7',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'ACTION_390_face_southwest_8',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_390_ret_9',
        "command": 'ret'
    }
]
