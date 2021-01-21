from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_968_shadow_off_0',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_968_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_968_set_sprite_sequence_2',
        "command": 'set_sprite_sequence',
        "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_968_walk_1_step_southeast_3',
        "command": 'walk_1_step_southeast'
    },
    {
        "identifier": 'ACTION_968_set_sprite_sequence_4',
        "command": 'set_sprite_sequence',
        "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_968_walk_to_xy_coords_5',
        "command": 'walk_to_xy_coords',
        "args": [16, 113]
    },
    {
        "identifier": 'ACTION_968_shirt_to_xy_coords_6',
        "command": 'shirt_to_xy_coords',
        "args": [14, 52]
    },
    {
        "identifier": 'ACTION_968_shift_southeast_steps_7',
        "command": 'shift_southeast_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_968_set_sprite_sequence_8',
        "command": 'set_sprite_sequence',
        "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_968_shirt_to_xy_coords_9',
        "command": 'shirt_to_xy_coords',
        "args": [6, 92]
    },
    {
        "identifier": 'ACTION_968_jmp_10',
        "command": 'jmp',
        "args": ['ACTION_965_shadow_off_0']
    }
]
