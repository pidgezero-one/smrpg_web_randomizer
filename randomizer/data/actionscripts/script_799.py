from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_799_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_799_set_sprite_sequence_1',
        "command": 'set_sprite_sequence',
        "args": [0, inc_sprite=4, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_799_pause_2',
        "command": 'pause',
        "args": [66]
    },
    {
        "identifier": 'ACTION_799_reset_properties_3',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_799_face_northwest_4',
        "command": 'face_northwest'
    },
    {
        "identifier": 'ACTION_799_set_animation_speed_5',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_799_ret_6',
        "command": 'ret'
    }
]
