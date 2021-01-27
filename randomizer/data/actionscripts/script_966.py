from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_966_shadow_off_0',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_966_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_966_set_sprite_sequence_2',
        "command": 'set_sprite_sequence',
        "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_966_walk_to_xy_coords_3',
        "command": 'walk_to_xy_coords',
        "args": [9, 99]
    },
    {
        "identifier": 'ACTION_966_shift_southeast_pixels_4',
        "command": 'shift_southeast_pixels',
        "args": [9]
    },
    {
        "identifier": 'ACTION_966_set_bit_5',
        "command": 'set_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'ACTION_966_walk_to_xy_coords_6',
        "command": 'walk_to_xy_coords',
        "args": [12, 105]
    },
    {
        "identifier": 'ACTION_966_shift_southeast_pixels_7',
        "command": 'shift_southeast_pixels',
        "args": [9]
    },
    {
        "identifier": 'ACTION_966_set_bit_8',
        "command": 'set_bit',
        "args": [0x7043, 2]
    },
    {
        "identifier": 'ACTION_966_walk_1_step_southeast_9',
        "command": 'walk_1_step_southeast'
    },
    {
        "identifier": 'ACTION_966_set_sprite_sequence_10',
        "command": 'set_sprite_sequence',
        "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_966_walk_to_xy_coords_11',
        "command": 'walk_to_xy_coords',
        "args": [16, 113]
    },
    {
        "identifier": 'ACTION_966_shirt_to_xy_coords_12',
        "command": 'shirt_to_xy_coords',
        "args": [14, 52]
    },
    {
        "identifier": 'ACTION_966_shift_southeast_steps_13',
        "command": 'shift_southeast_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_966_set_sprite_sequence_14',
        "command": 'set_sprite_sequence',
        "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_966_shirt_to_xy_coords_15',
        "command": 'shirt_to_xy_coords',
        "args": [6, 92]
    },
    {
        "identifier": 'ACTION_966_jmp_16',
        "command": 'jmp',
        "args": ['ACTION_965_shadow_off_0']
    }
]
