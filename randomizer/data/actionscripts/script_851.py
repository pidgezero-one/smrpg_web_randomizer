from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_851_floating_off_0',
        "command": 'floating_off'
    },
    {
        "identifier": 'ACTION_851_shadow_off_1',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_851_set_priority_2',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_851_overwrite_solidity_3',
        "command": 'overwrite_solidity',
        "args": [[]]
    },
    {
        "identifier": 'ACTION_851_face_southeast_4',
        "command": 'face_southeast'
    },
    {
        "identifier": 'ACTION_851_set_sprite_sequence_5',
        "command": 'set_sprite_sequence',
        "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_851_set_animation_speed_6',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_851_play_sound_7',
        "command": 'play_sound',
        "args": [Sounds._024_TAPPING_FEET, 4]
    },
    {
        "identifier": 'ACTION_851_pause_8',
        "command": 'pause',
        "args": [80]
    },
    {
        "identifier": 'ACTION_851_play_sound_9',
        "command": 'play_sound',
        "args": [Sounds._011_WHOOSH_AWAY, 4]
    },
    {
        "identifier": 'ACTION_851_set_animation_speed_10',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_851_walk_to_xy_coords_11',
        "command": 'walk_to_xy_coords',
        "args": [23, 76]
    },
    {
        "identifier": 'ACTION_851_visibility_off_12',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_851_ret_13',
        "command": 'ret'
    }
]
