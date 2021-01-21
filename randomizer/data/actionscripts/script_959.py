from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_959_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_959_shadow_off_1',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_959_set_sprite_sequence_2',
        "command": 'set_sprite_sequence',
        "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_959_shift_west_pixels_3',
        "command": 'shift_west_pixels',
        "args": [4]
    },
    {
        "identifier": 'ACTION_959_set_animation_speed_4',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_959_set_bit_5',
        "command": 'set_bit',
        "args": [0x7044, 1]
    },
    {
        "identifier": 'ACTION_959_shift_north_steps_6',
        "command": 'shift_north_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_959_shift_north_pixels_7',
        "command": 'shift_north_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_959_jmp_if_bit_set_8',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 0, 'ACTION_959_shift_z_up_steps_11']
    },
    {
        "identifier": 'ACTION_959_pause_9',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_959_jmp_10',
        "command": 'jmp',
        "args": ['ACTION_959_jmp_if_bit_set_8']
    },
    {
        "identifier": 'ACTION_959_shift_z_up_steps_11',
        "command": 'shift_z_up_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_959_walk_to_xy_coords_12',
        "command": 'walk_to_xy_coords',
        "args": [3, 88]
    },
    {
        "identifier": 'ACTION_959_shadow_on_13',
        "command": 'shadow_on'
    },
    {
        "identifier": 'ACTION_959_set_animation_speed_14',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_959_shift_southeast_pixels_15',
        "command": 'shift_southeast_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_959_set_animation_speed_16',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_959_shift_z_down_steps_17',
        "command": 'shift_z_down_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_959_pause_18',
        "command": 'pause',
        "args": [12]
    },
    {
        "identifier": 'ACTION_959_clear_bit_19',
        "command": 'clear_bit',
        "args": [0x7044, 0]
    },
    {
        "identifier": 'ACTION_959_clear_bit_20',
        "command": 'clear_bit',
        "args": [0x7044, 1]
    },
    {
        "identifier": 'ACTION_959_walk_to_xy_coords_21',
        "command": 'walk_to_xy_coords',
        "args": [10, 103]
    },
    {
        "identifier": 'ACTION_959_shirt_to_xy_coords_22',
        "command": 'shirt_to_xy_coords',
        "args": [1, 77]
    },
    {
        "identifier": 'ACTION_959_jmp_if_bit_set_23',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 2, 'ACTION_959_ret_25']
    },
    {
        "identifier": 'ACTION_959_jmp_24',
        "command": 'jmp',
        "args": ['ACTION_959_set_animation_speed_0']
    },
    {
        "identifier": 'ACTION_959_ret_25',
        "command": 'ret'
    }
]
