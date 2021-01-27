from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_384_sequence_looping_on_0',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_384_set_sprite_sequence_1',
        "command": 'set_sprite_sequence',
        "args": [6, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_384_pause_2',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'ACTION_384_set_animation_speed_3',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_384_play_sound_4',
        "command": 'play_sound',
        "args": [Sounds._056_SHAKE_HEAD, 4]
    },
    {
        "identifier": 'ACTION_384_set_sprite_sequence_5',
        "command": 'set_sprite_sequence',
        "args": [8, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_384_pause_6',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'ACTION_384_set_animation_speed_7',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_384_set_sprite_sequence_8',
        "command": 'set_sprite_sequence',
        "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_384_sequence_looping_off_9',
        "command": 'sequence_looping_off'
    },
    {
        "identifier": 'ACTION_384_ret_10',
        "command": 'ret'
    }
]
