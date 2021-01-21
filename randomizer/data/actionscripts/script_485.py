from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_485_set_vram_priority_0',
        "command": 'set_vram_priority',
        "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
    },
    {
        "identifier": 'ACTION_485_set_sprite_sequence_1',
        "command": 'set_sprite_sequence',
        "args": [0, inc_sprite=3, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_485_shirt_to_xy_coords_2',
        "command": 'shirt_to_xy_coords',
        "args": [3, 74]
    },
    {
        "identifier": 'ACTION_485_set_animation_speed_3',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_485_shift_southeast_pixels_4',
        "command": 'shift_southeast_pixels',
        "args": [4]
    },
    {
        "identifier": 'ACTION_485_shift_north_pixels_5',
        "command": 'shift_north_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_485_set_sprite_sequence_6',
        "command": 'set_sprite_sequence',
        "args": [0, inc_sprite=3, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_485_pause_7',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'ACTION_485_set_sprite_sequence_8',
        "command": 'set_sprite_sequence',
        "args": [0, inc_sprite=3, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_485_pause_9',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'ACTION_485_jmp_if_bit_set_10',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'ACTION_485_pause_12']
    },
    {
        "identifier": 'ACTION_485_jmp_11',
        "command": 'jmp',
        "args": ['ACTION_485_set_sprite_sequence_6']
    },
    {
        "identifier": 'ACTION_485_pause_12',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'ACTION_485_shift_southeast_pixels_13',
        "command": 'shift_southeast_pixels',
        "args": [4]
    },
    {
        "identifier": 'ACTION_485_db_14',
        "command": 'db',
        "args": [0x20, 0x04]
    },
    {
        "identifier": 'ACTION_485_db_15',
        "command": 'db',
        "args": [0x25, 0x00, 0x0f, 0x80, 0xff]
    },
    {
        "identifier": 'ACTION_485_pause_16',
        "command": 'pause',
        "args": [48]
    },
    {
        "identifier": 'ACTION_485_bpl_26_27_28_17',
        "command": 'bpl_26_27_28'
    },
    {
        "identifier": 'ACTION_485_ret_18',
        "command": 'ret'
    }
]
