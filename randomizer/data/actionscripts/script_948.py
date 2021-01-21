from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_948_shadow_off_0',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_948_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_948_walk_to_xy_coords_2',
        "command": 'walk_to_xy_coords',
        "args": [11, 38]
    },
    {
        "identifier": 'ACTION_948_shift_southeast_pixels_3',
        "command": 'shift_southeast_pixels',
        "args": [11]
    },
    {
        "identifier": 'ACTION_948_set_bit_4',
        "command": 'set_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'ACTION_948_walk_to_xy_coords_5',
        "command": 'walk_to_xy_coords',
        "args": [11, 39]
    },
    {
        "identifier": 'ACTION_948_visibility_off_6',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_948_walk_to_xy_coords_7',
        "command": 'walk_to_xy_coords',
        "args": [16, 49]
    },
    {
        "identifier": 'ACTION_948_shirt_to_xy_coords_8',
        "command": 'shirt_to_xy_coords',
        "args": [3, 88]
    },
    {
        "identifier": 'ACTION_948_shift_southeast_steps_9',
        "command": 'shift_southeast_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_948_shirt_to_xy_coords_10',
        "command": 'shirt_to_xy_coords',
        "args": [6, 28]
    },
    {
        "identifier": 'ACTION_948_visibility_on_11',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_948_jmp_12',
        "command": 'jmp',
        "args": ['ACTION_948_shadow_off_0']
    }
]
