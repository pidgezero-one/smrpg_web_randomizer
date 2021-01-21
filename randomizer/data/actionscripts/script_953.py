from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_953_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_953_shirt_to_xy_coords_1',
        "command": 'shirt_to_xy_coords',
        "args": [3, 70]
    },
    {
        "identifier": 'ACTION_953_set_sprite_sequence_2',
        "command": 'set_sprite_sequence',
        "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_953_shift_north_steps_3',
        "command": 'shift_north_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_953_set_vram_priority_4',
        "command": 'set_vram_priority',
        "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
    },
    {
        "identifier": 'ACTION_953_db_5',
        "command": 'db',
        "args": [0x20, 0x03]
    },
    {
        "identifier": 'ACTION_953_db_6',
        "command": 'db',
        "args": [0x24, 0x00, 0x01, 0x50, 0x01]
    },
    {
        "identifier": 'ACTION_953_pause_7',
        "command": 'pause',
        "args": [48]
    },
    {
        "identifier": 'ACTION_953_set_vram_priority_8',
        "command": 'set_vram_priority',
        "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
    },
    {
        "identifier": 'ACTION_953_pause_9',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'ACTION_953_bpl_26_27_28_10',
        "command": 'bpl_26_27_28'
    },
    {
        "identifier": 'ACTION_953_pause_11',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_953_set_sprite_sequence_12',
        "command": 'set_sprite_sequence',
        "args": [3, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_953_shift_northeast_steps_13',
        "command": 'shift_northeast_steps',
        "args": [4]
    },
    {
        "identifier": 'ACTION_953_shift_northeast_pixels_14',
        "command": 'shift_northeast_pixels',
        "args": [11]
    },
    {
        "identifier": 'ACTION_953_db_15',
        "command": 'db',
        "args": [0x20, 0x03]
    },
    {
        "identifier": 'ACTION_953_db_16',
        "command": 'db',
        "args": [0x24, 0xc0, 0x01, 0xa0, 0x02]
    },
    {
        "identifier": 'ACTION_953_pause_17',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'ACTION_953_set_sprite_sequence_18',
        "command": 'set_sprite_sequence',
        "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_953_pause_19',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'ACTION_953_bpl_26_27_28_20',
        "command": 'bpl_26_27_28'
    },
    {
        "identifier": 'ACTION_953_shift_southeast_steps_21',
        "command": 'shift_southeast_steps',
        "args": [16]
    },
    {
        "identifier": 'ACTION_953_shirt_to_xy_coords_22',
        "command": 'shirt_to_xy_coords',
        "args": [8, 35]
    },
    {
        "identifier": 'ACTION_953_shift_southeast_steps_23',
        "command": 'shift_southeast_steps',
        "args": [5]
    },
    {
        "identifier": 'ACTION_953_jmp_24',
        "command": 'jmp',
        "args": ['ACTION_953_set_animation_speed_0']
    }
]
