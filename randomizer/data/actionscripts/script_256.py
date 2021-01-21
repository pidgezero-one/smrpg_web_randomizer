from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_256_set_700C_to_current_level_0',
        "command": 'set_700C_to_current_level'
    },
    {
        "identifier": 'ACTION_256_jmp_if_var_equals_short_1',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 117, 'ACTION_256_reset_properties_8']
    },
    {
        "identifier": 'ACTION_256_reset_properties_2',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_256_face_northeast_3',
        "command": 'face_northeast'
    },
    {
        "identifier": 'ACTION_256_set_animation_speed_4',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_256_set_animation_speed_5',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_256_walk_to_xy_coords_6',
        "command": 'walk_to_xy_coords',
        "args": [5, 109]
    },
    {
        "identifier": 'ACTION_256_ret_7',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_256_reset_properties_8',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_256_face_northeast_9',
        "command": 'face_northeast'
    },
    {
        "identifier": 'ACTION_256_set_animation_speed_10',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_256_set_animation_speed_11',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_256_walk_to_xy_coords_12',
        "command": 'walk_to_xy_coords',
        "args": [25, 78]
    },
    {
        "identifier": 'ACTION_256_face_northeast_13',
        "command": 'face_northeast'
    },
    {
        "identifier": 'ACTION_256_ret_14',
        "command": 'ret'
    }
]
