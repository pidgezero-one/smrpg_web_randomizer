from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_589_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_589_visibility_on_1',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_589_set_sprite_sequence_2',
        "command": 'set_sprite_sequence',
        "args": [10, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_589_pause_3',
        "command": 'pause',
        "args": [12]
    },
    {
        "identifier": 'ACTION_589_set_sprite_sequence_4',
        "command": 'set_sprite_sequence',
        "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_589_set_animation_speed_5',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_589_sequence_looping_on_6',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_589_ret_7',
        "command": 'ret'
    }
]
