from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_570_set_short_0',
        "command": 'set_short',
        "args": [0x7012, 0x0006]
    },
    {
        "identifier": 'ACTION_570_set_priority_1',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_570_set_animation_speed_2',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_570_visibility_on_3',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_570_set_sprite_sequence_4',
        "command": 'set_sprite_sequence',
        "args": [10, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_570_pause_5',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'ACTION_570_set_sprite_sequence_6',
        "command": 'set_sprite_sequence',
        "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_570_start_loop_n_times_7',
        "command": 'start_loop_n_times',
        "args": [5]
    },
    {
        "identifier": 'ACTION_570_set_bit_8',
        "command": 'set_bit',
        "args": [0x7044, 3]
    },
    {
        "identifier": 'ACTION_570_pause_9',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'ACTION_570_clear_bit_10',
        "command": 'clear_bit',
        "args": [0x7044, 3]
    },
    {
        "identifier": 'ACTION_570_set_animation_speed_11',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_570_shift_southeast_pixels_12',
        "command": 'shift_southeast_pixels',
        "args": [10]
    },
    {
        "identifier": 'ACTION_570_set_animation_speed_13',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_570_shift_southeast_pixels_14',
        "command": 'shift_southeast_pixels',
        "args": [4]
    },
    {
        "identifier": 'ACTION_570_set_animation_speed_15',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_570_shift_southeast_pixels_16',
        "command": 'shift_southeast_pixels',
        "args": [2]
    },
    {
        "identifier": 'ACTION_570_dec_short_17',
        "command": 'dec_short',
        "args": [0x7012]
    },
    {
        "identifier": 'ACTION_570_end_loop_18',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_570_set_sprite_sequence_19',
        "command": 'set_sprite_sequence',
        "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_570_start_loop_n_times_20',
        "command": 'start_loop_n_times',
        "args": [5]
    },
    {
        "identifier": 'ACTION_570_set_bit_21',
        "command": 'set_bit',
        "args": [0x7044, 3]
    },
    {
        "identifier": 'ACTION_570_pause_22',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'ACTION_570_clear_bit_23',
        "command": 'clear_bit',
        "args": [0x7044, 3]
    },
    {
        "identifier": 'ACTION_570_set_animation_speed_24',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_570_shift_northwest_pixels_25',
        "command": 'shift_northwest_pixels',
        "args": [10]
    },
    {
        "identifier": 'ACTION_570_set_animation_speed_26',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_570_shift_northwest_pixels_27',
        "command": 'shift_northwest_pixels',
        "args": [4]
    },
    {
        "identifier": 'ACTION_570_set_animation_speed_28',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_570_shift_northwest_pixels_29',
        "command": 'shift_northwest_pixels',
        "args": [2]
    },
    {
        "identifier": 'ACTION_570_inc_short_30',
        "command": 'inc_short',
        "args": [0x7012]
    },
    {
        "identifier": 'ACTION_570_end_loop_31',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_570_jmp_32',
        "command": 'jmp',
        "args": ['ACTION_570_set_sprite_sequence_6']
    }
]
