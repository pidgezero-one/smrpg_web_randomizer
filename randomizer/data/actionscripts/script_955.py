from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_955_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_955_set_sprite_sequence_1',
        "command": 'set_sprite_sequence',
        "args": [3, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_955_walk_to_xy_coords_2',
        "command": 'walk_to_xy_coords',
        "args": [7, 75]
    },
    {
        "identifier": 'ACTION_955_shift_northeast_pixels_3',
        "command": 'shift_northeast_pixels',
        "args": [11]
    },
    {
        "identifier": 'ACTION_955_db_4',
        "command": 'db',
        "args": [0x20, 0x03]
    },
    {
        "identifier": 'ACTION_955_db_5',
        "command": 'db',
        "args": [0x24, 0xc0, 0x01, 0xa0, 0x02]
    },
    {
        "identifier": 'ACTION_955_pause_6',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'ACTION_955_set_sprite_sequence_7',
        "command": 'set_sprite_sequence',
        "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_955_pause_8',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'ACTION_955_bpl_26_27_28_9',
        "command": 'bpl_26_27_28'
    },
    {
        "identifier": 'ACTION_955_shift_southeast_steps_10',
        "command": 'shift_southeast_steps',
        "args": [16]
    },
    {
        "identifier": 'ACTION_955_shirt_to_xy_coords_11',
        "command": 'shirt_to_xy_coords',
        "args": [8, 35]
    },
    {
        "identifier": 'ACTION_955_shift_southeast_steps_12',
        "command": 'shift_southeast_steps',
        "args": [5]
    },
    {
        "identifier": 'ACTION_955_set_vram_priority_13',
        "command": 'set_vram_priority',
        "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
    },
    {
        "identifier": 'ACTION_955_jmp_14',
        "command": 'jmp',
        "args": ['ACTION_953_set_animation_speed_0']
    }
]
