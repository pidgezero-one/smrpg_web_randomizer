from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_222_transfer_xyzf_pixels_0',
        "command": 'transfer_xyzf_pixels',
        "args": [0, 0, 2, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_222_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_222_sequence_looping_on_2',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_222_db_3',
        "command": 'db',
        "args": [0x20, 0x04]
    },
    {
        "identifier": 'ACTION_222_embedded_animation_routine_4',
        "command": 'embedded_animation_routine',
        "args": [0x28, 0x00, 0x00, 0x00, 0x00, 0x00, 0x40, 0x00, 0x02, 0x00, 0x01, 0x00, 0x00, 0x00, 0x08, 0x80]
    },
    {
        "identifier": 'ACTION_222_fixed_f_coord_on_5',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_222_set_animation_speed_6',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_222_walk_1_step_southeast_7',
        "command": 'walk_1_step_southeast'
    },
    {
        "identifier": 'ACTION_222_pause_8',
        "command": 'pause',
        "args": [90]
    },
    {
        "identifier": 'ACTION_222_fixed_f_coord_off_9',
        "command": 'fixed_f_coord_off'
    },
    {
        "identifier": 'ACTION_222_walk_1_step_northeast_10',
        "command": 'walk_1_step_northeast'
    },
    {
        "identifier": 'ACTION_222_jmp_if_random_above_128_11',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_222_walk_1_step_southeast_21']
    },
    {
        "identifier": 'ACTION_222_shift_northeast_steps_12',
        "command": 'shift_northeast_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_222_walk_1_step_northwest_13',
        "command": 'walk_1_step_northwest'
    },
    {
        "identifier": 'ACTION_222_pause_14',
        "command": 'pause',
        "args": [120]
    },
    {
        "identifier": 'ACTION_222_fixed_f_coord_on_15',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_222_walk_1_step_southeast_16',
        "command": 'walk_1_step_southeast'
    },
    {
        "identifier": 'ACTION_222_pause_17',
        "command": 'pause',
        "args": [90]
    },
    {
        "identifier": 'ACTION_222_fixed_f_coord_off_18',
        "command": 'fixed_f_coord_off'
    },
    {
        "identifier": 'ACTION_222_shift_southwest_steps_19',
        "command": 'shift_southwest_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_222_jmp_if_random_above_128_20',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_222_walk_1_step_southwest_28']
    },
    {
        "identifier": 'ACTION_222_walk_1_step_southeast_21',
        "command": 'walk_1_step_southeast'
    },
    {
        "identifier": 'ACTION_222_shift_southeast_pixels_22',
        "command": 'shift_southeast_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_222_face_northeast_23',
        "command": 'face_northeast'
    },
    {
        "identifier": 'ACTION_222_pause_24',
        "command": 'pause',
        "args": [120]
    },
    {
        "identifier": 'ACTION_222_walk_1_step_northwest_25',
        "command": 'walk_1_step_northwest'
    },
    {
        "identifier": 'ACTION_222_shift_northwest_pixels_26',
        "command": 'shift_northwest_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_222_jmp_if_random_above_128_27',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_222_shift_northeast_steps_12']
    },
    {
        "identifier": 'ACTION_222_walk_1_step_southwest_28',
        "command": 'walk_1_step_southwest'
    },
    {
        "identifier": 'ACTION_222_walk_1_step_northwest_29',
        "command": 'walk_1_step_northwest'
    },
    {
        "identifier": 'ACTION_222_pause_30',
        "command": 'pause',
        "args": [120]
    },
    {
        "identifier": 'ACTION_222_fixed_f_coord_on_31',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_222_jmp_32',
        "command": 'jmp',
        "args": ['ACTION_222_walk_1_step_southeast_7']
    }
]
