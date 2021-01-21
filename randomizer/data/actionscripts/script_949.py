from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_949_shadow_off_0',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_949_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_949_visibility_off_2',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_949_walk_to_xy_coords_3',
        "command": 'walk_to_xy_coords',
        "args": [16, 49]
    },
    {
        "identifier": 'ACTION_949_shirt_to_xy_coords_4',
        "command": 'shirt_to_xy_coords',
        "args": [3, 88]
    },
    {
        "identifier": 'ACTION_949_shift_southeast_steps_5',
        "command": 'shift_southeast_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_949_shirt_to_xy_coords_6',
        "command": 'shirt_to_xy_coords',
        "args": [6, 28]
    },
    {
        "identifier": 'ACTION_949_visibility_on_7',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_949_jmp_8',
        "command": 'jmp',
        "args": ['ACTION_948_shadow_off_0']
    }
]
