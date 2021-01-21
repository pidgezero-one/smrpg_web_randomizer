from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_90_pause_0',
        "command": 'pause',
        "args": [70]
    },
    {
        "identifier": 'ACTION_90_set_sprite_sequence_1',
        "command": 'set_sprite_sequence',
        "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_90_fixed_f_coord_on_2',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_90_set_animation_speed_3',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_90_sequence_looping_on_4',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_90_start_loop_n_times_5',
        "command": 'start_loop_n_times',
        "args": [6]
    },
    {
        "identifier": 'ACTION_90_set_animation_speed_6',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_90_shift_west_pixels_7',
        "command": 'shift_west_pixels',
        "args": [1]
    },
    {
        "identifier": 'ACTION_90_pause_8',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_90_set_animation_speed_9',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_90_shift_northwest_pixels_10',
        "command": 'shift_northwest_pixels',
        "args": [1]
    },
    {
        "identifier": 'ACTION_90_pause_11',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_90_set_animation_speed_12',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_90_shift_southeast_pixels_13',
        "command": 'shift_southeast_pixels',
        "args": [1]
    },
    {
        "identifier": 'ACTION_90_pause_14',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_90_set_animation_speed_15',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_90_shift_east_pixels_16',
        "command": 'shift_east_pixels',
        "args": [1]
    },
    {
        "identifier": 'ACTION_90_pause_17',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_90_set_animation_speed_18',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_90_shift_east_pixels_19',
        "command": 'shift_east_pixels',
        "args": [1]
    },
    {
        "identifier": 'ACTION_90_pause_20',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_90_set_animation_speed_21',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_90_shift_northeast_pixels_22',
        "command": 'shift_northeast_pixels',
        "args": [1]
    },
    {
        "identifier": 'ACTION_90_pause_23',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_90_set_animation_speed_24',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_90_shift_southwest_pixels_25',
        "command": 'shift_southwest_pixels',
        "args": [1]
    },
    {
        "identifier": 'ACTION_90_pause_26',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_90_set_animation_speed_27',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_90_shift_west_pixels_28',
        "command": 'shift_west_pixels',
        "args": [1]
    },
    {
        "identifier": 'ACTION_90_pause_29',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_90_end_loop_30',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_90_set_sprite_sequence_31',
        "command": 'set_sprite_sequence',
        "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_90_jmp_32',
        "command": 'jmp',
        "args": ['ACTION_154_fixed_f_coord_on_0']
    }
]
