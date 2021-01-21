from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_571_clear_bit_0',
        "command": 'clear_bit',
        "args": [0x7044, 3]
    },
    {
        "identifier": 'ACTION_571_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_571_set_sprite_sequence_2',
        "command": 'set_sprite_sequence',
        "args": [10, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_571_pause_3',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'ACTION_571_set_sprite_sequence_4',
        "command": 'set_sprite_sequence',
        "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_571_fixed_f_coord_on_5',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_571_sequence_looping_on_6',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_571_set_animation_speed_7',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_571_shift_west_pixels_8',
        "command": 'shift_west_pixels',
        "args": [1]
    },
    {
        "identifier": 'ACTION_571_pause_9',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_571_set_animation_speed_10',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_571_shift_northwest_pixels_11',
        "command": 'shift_northwest_pixels',
        "args": [1]
    },
    {
        "identifier": 'ACTION_571_pause_12',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_571_set_animation_speed_13',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_571_shift_southeast_pixels_14',
        "command": 'shift_southeast_pixels',
        "args": [1]
    },
    {
        "identifier": 'ACTION_571_pause_15',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_571_set_animation_speed_16',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_571_shift_east_pixels_17',
        "command": 'shift_east_pixels',
        "args": [1]
    },
    {
        "identifier": 'ACTION_571_pause_18',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_571_set_animation_speed_19',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_571_shift_east_pixels_20',
        "command": 'shift_east_pixels',
        "args": [1]
    },
    {
        "identifier": 'ACTION_571_pause_21',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_571_set_animation_speed_22',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_571_shift_northeast_pixels_23',
        "command": 'shift_northeast_pixels',
        "args": [1]
    },
    {
        "identifier": 'ACTION_571_pause_24',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_571_set_animation_speed_25',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_571_shift_southwest_pixels_26',
        "command": 'shift_southwest_pixels',
        "args": [1]
    },
    {
        "identifier": 'ACTION_571_pause_27',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_571_set_animation_speed_28',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_571_shift_west_pixels_29',
        "command": 'shift_west_pixels',
        "args": [1]
    },
    {
        "identifier": 'ACTION_571_pause_30',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_571_jmp_31',
        "command": 'jmp',
        "args": ['ACTION_571_set_sprite_sequence_4']
    },
    {
        "identifier": 'ACTION_571_ret_32',
        "command": 'ret'
    }
]
