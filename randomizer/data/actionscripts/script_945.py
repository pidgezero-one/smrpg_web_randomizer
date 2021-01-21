from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_945_shadow_off_0',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_945_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_945_walk_to_xy_coords_2',
        "command": 'walk_to_xy_coords',
        "args": [16, 49]
    },
    {
        "identifier": 'ACTION_945_shirt_to_xy_coords_3',
        "command": 'shirt_to_xy_coords',
        "args": [3, 88]
    },
    {
        "identifier": 'ACTION_945_shift_southeast_steps_4',
        "command": 'shift_southeast_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_945_shirt_to_xy_coords_5',
        "command": 'shirt_to_xy_coords',
        "args": [6, 28]
    },
    {
        "identifier": 'ACTION_945_jmp_6',
        "command": 'jmp',
        "args": ['ACTION_945_shadow_off_0']
    }
]
