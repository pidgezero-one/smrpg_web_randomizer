from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_958_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_958_set_priority_1',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_958_set_vram_priority_2',
        "command": 'set_vram_priority',
        "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
    },
    {
        "identifier": 'ACTION_958_shift_east_pixels_3',
        "command": 'shift_east_pixels',
        "args": [12]
    },
    {
        "identifier": 'ACTION_958_set_animation_speed_4',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_958_set_sprite_sequence_5',
        "command": 'set_sprite_sequence',
        "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_958_shift_z_down_steps_6',
        "command": 'shift_z_down_steps',
        "args": [4]
    },
    {
        "identifier": 'ACTION_958_shift_z_down_pixels_7',
        "command": 'shift_z_down_pixels',
        "args": [3]
    },
    {
        "identifier": 'ACTION_958_pause_8',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'ACTION_958_set_sprite_sequence_9',
        "command": 'set_sprite_sequence',
        "args": [3, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_958_pause_10',
        "command": 'pause',
        "args": [11]
    },
    {
        "identifier": 'ACTION_958_set_sprite_sequence_11',
        "command": 'set_sprite_sequence',
        "args": [4, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_958_pause_12',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_958_set_bit_13',
        "command": 'set_bit',
        "args": [0x7044, 0]
    },
    {
        "identifier": 'ACTION_958_shift_z_up_steps_14',
        "command": 'shift_z_up_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_958_walk_to_xy_coords_15',
        "command": 'walk_to_xy_coords',
        "args": [3, 88]
    },
    {
        "identifier": 'ACTION_958_set_animation_speed_16',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_958_shift_southeast_pixels_17',
        "command": 'shift_southeast_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_958_set_animation_speed_18',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_958_shift_z_down_steps_19',
        "command": 'shift_z_down_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_958_pause_20',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'ACTION_958_set_sprite_sequence_21',
        "command": 'set_sprite_sequence',
        "args": [3, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_958_pause_22',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'ACTION_958_set_sprite_sequence_23',
        "command": 'set_sprite_sequence',
        "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_958_pause_24',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'ACTION_958_shift_z_up_steps_25',
        "command": 'shift_z_up_steps',
        "args": [4]
    },
    {
        "identifier": 'ACTION_958_shift_z_up_pixels_26',
        "command": 'shift_z_up_pixels',
        "args": [3]
    },
    {
        "identifier": 'ACTION_958_walk_to_xy_coords_27',
        "command": 'walk_to_xy_coords',
        "args": [1, 72]
    },
    {
        "identifier": 'ACTION_958_jmp_28',
        "command": 'jmp',
        "args": ['ACTION_958_shift_east_pixels_3']
    }
]
