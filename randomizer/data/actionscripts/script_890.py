from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_890_set_700C_to_current_level_0',
        "command": 'set_700C_to_current_level'
    },
    {
        "identifier": 'ACTION_890_jmp_if_var_equals_short_1',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 117, 'ACTION_890_pause_23']
    },
    {
        "identifier": 'ACTION_890_pause_2',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_890_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 2, 'ACTION_890_pause_5']
    },
    {
        "identifier": 'ACTION_890_jmp_4',
        "command": 'jmp',
        "args": ['ACTION_890_pause_2']
    },
    {
        "identifier": 'ACTION_890_pause_5',
        "command": 'pause',
        "args": [90]
    },
    {
        "identifier": 'ACTION_890_face_southwest_6',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_890_set_sprite_sequence_7',
        "command": 'set_sprite_sequence',
        "args": [5, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_890_jmp_if_random_above_128_8',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_890_set_animation_speed_11']
    },
    {
        "identifier": 'ACTION_890_set_animation_speed_9',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_890_jmp_10',
        "command": 'jmp',
        "args": ['ACTION_890_walk_1_step_south_12']
    },
    {
        "identifier": 'ACTION_890_set_animation_speed_11',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_890_walk_1_step_south_12',
        "command": 'walk_1_step_south'
    },
    {
        "identifier": 'ACTION_890_set_animation_speed_13',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_890_shift_southwest_pixels_14',
        "command": 'shift_southwest_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_890_jmp_if_random_above_128_15',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_890_set_animation_speed_18']
    },
    {
        "identifier": 'ACTION_890_set_animation_speed_16',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_890_jmp_17',
        "command": 'jmp',
        "args": ['ACTION_890_walk_1_step_west_19']
    },
    {
        "identifier": 'ACTION_890_set_animation_speed_18',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_890_walk_1_step_west_19',
        "command": 'walk_1_step_west'
    },
    {
        "identifier": 'ACTION_890_set_animation_speed_20',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_890_shift_southwest_pixels_21',
        "command": 'shift_southwest_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_890_jmp_22',
        "command": 'jmp',
        "args": ['ACTION_890_jmp_if_random_above_128_8']
    },
    {
        "identifier": 'ACTION_890_pause_23',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_890_jmp_if_bit_set_24',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 2, 'ACTION_890_pause_26']
    },
    {
        "identifier": 'ACTION_890_jmp_25',
        "command": 'jmp',
        "args": ['ACTION_890_pause_23']
    },
    {
        "identifier": 'ACTION_890_pause_26',
        "command": 'pause',
        "args": [90]
    },
    {
        "identifier": 'ACTION_890_face_southwest_27',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_890_set_sprite_sequence_28',
        "command": 'set_sprite_sequence',
        "args": [5, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_890_jmp_if_random_above_128_29',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_890_set_animation_speed_32']
    },
    {
        "identifier": 'ACTION_890_set_animation_speed_30',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_890_jmp_31',
        "command": 'jmp',
        "args": ['ACTION_890_walk_1_step_south_33']
    },
    {
        "identifier": 'ACTION_890_set_animation_speed_32',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_890_walk_1_step_south_33',
        "command": 'walk_1_step_south'
    },
    {
        "identifier": 'ACTION_890_set_animation_speed_34',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_890_shift_southwest_pixels_35',
        "command": 'shift_southwest_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_890_jmp_if_random_above_128_36',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_890_set_animation_speed_39']
    },
    {
        "identifier": 'ACTION_890_set_animation_speed_37',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_890_jmp_38',
        "command": 'jmp',
        "args": ['ACTION_890_walk_1_step_west_40']
    },
    {
        "identifier": 'ACTION_890_set_animation_speed_39',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_890_walk_1_step_west_40',
        "command": 'walk_1_step_west'
    },
    {
        "identifier": 'ACTION_890_set_animation_speed_41',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_890_shift_southwest_pixels_42',
        "command": 'shift_southwest_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_890_jmp_43',
        "command": 'jmp',
        "args": ['ACTION_890_jmp_if_random_above_128_29']
    }
]
