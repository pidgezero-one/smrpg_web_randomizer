from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_971_set_vram_priority_0',
        "command": 'set_vram_priority',
        "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
    },
    {
        "identifier": 'ACTION_971_set_priority_1',
        "command": 'set_priority',
        "args": [1]
    },
    {
        "identifier": 'ACTION_971_visibility_on_2',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_971_set_sprite_sequence_3',
        "command": 'set_sprite_sequence',
        "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_971_db_4',
        "command": 'db',
        "args": [0x20, 0x04]
    },
    {
        "identifier": 'ACTION_971_embedded_animation_routine_5',
        "command": 'embedded_animation_routine',
        "args": [0x28]
    },
    {
        "identifier": 'ACTION_971_shift_north_pixels_6',
        "command": 'shift_north_pixels',
        "args": [5]
    },
    {
        "identifier": 'ACTION_971_set_animation_speed_7',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_971_walk_to_xy_coords_8',
        "command": 'walk_to_xy_coords',
        "args": [5, 6]
    },
    {
        "identifier": 'ACTION_971_shirt_to_xy_coords_9',
        "command": 'shirt_to_xy_coords',
        "args": [5, 8]
    },
    {
        "identifier": 'ACTION_971_set_animation_speed_10',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_971_shift_south_pixels_11',
        "command": 'shift_south_pixels',
        "args": [15]
    },
    {
        "identifier": 'ACTION_971_shift_southwest_pixels_12',
        "command": 'shift_southwest_pixels',
        "args": [20]
    },
    {
        "identifier": 'ACTION_971_set_animation_speed_13',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_971_set_sprite_sequence_14',
        "command": 'set_sprite_sequence',
        "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_971_shift_southwest_steps_15',
        "command": 'shift_southwest_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_971_shift_southwest_pixels_16',
        "command": 'shift_southwest_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_971_pause_17',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_971_db_18',
        "command": 'db',
        "args": [0x20, 0x05]
    },
    {
        "identifier": 'ACTION_971_embedded_animation_routine_19',
        "command": 'embedded_animation_routine',
        "args": [0x26]
    },
    {
        "identifier": 'ACTION_971_pause_20',
        "command": 'pause',
        "args": [511]
    },
    {
        "identifier": 'ACTION_971_ret_21',
        "command": 'ret'
    }
]
