from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_162_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7078, 1, 'ACTION_162_set_animation_speed_57']
    },
    {
        "identifier": 'ACTION_162_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7078, 0, 'ACTION_162_set_animation_speed_38']
    },
    {
        "identifier": 'ACTION_162_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x7077, 7, 'ACTION_162_set_animation_speed_18']
    },
    {
        "identifier": 'ACTION_162_visibility_on_3',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_162_set_bit_4',
        "command": 'set_bit',
        "args": [0x7077, 7]
    },
    {
        "identifier": 'ACTION_162_sequence_looping_on_5',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_162_set_animation_speed_6',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FASTER, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_162_play_sound_7',
        "command": 'play_sound',
        "args": [Sounds._033_JUMPING_BOUNCING_FISH, 4]
    },
    {
        "identifier": 'ACTION_162_jump_to_height_8',
        "command": 'jump_to_height',
        "args": [128]
    },
    {
        "identifier": 'ACTION_162_walk_to_xy_coords_9',
        "command": 'walk_to_xy_coords',
        "args": [20, 108]
    },
    {
        "identifier": 'ACTION_162_shift_north_steps_10',
        "command": 'shift_north_steps',
        "args": [7]
    },
    {
        "identifier": 'ACTION_162_start_loop_n_times_11',
        "command": 'start_loop_n_times',
        "args": [1]
    },
    {
        "identifier": 'ACTION_162_shift_northeast_steps_12',
        "command": 'shift_northeast_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_162_set_animation_speed_13',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_162_shift_northeast_steps_14',
        "command": 'shift_northeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_162_set_animation_speed_15',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FASTER, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_162_end_loop_16',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_162_shift_northwest_steps_17',
        "command": 'shift_northwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_162_set_animation_speed_18',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FASTER, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_162_transfer_to_xyzf_19',
        "command": 'transfer_to_xyzf',
        "args": [24, 82, 0, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_162_visibility_on_20',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_162_face_southwest_21',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_162_pause_22',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_162_db_23',
        "command": 'db',
        "args": [0x3a, 0x00, 0x00, 0x04, 0x06, 0x20]
    },
    {
        "identifier": 'ACTION_162_jmp_24',
        "command": 'jmp',
        "args": ['ACTION_162_pause_22']
    },
    {
        "identifier": 'ACTION_162_set_bit_25',
        "command": 'set_bit',
        "args": [0x7078, 0]
    },
    {
        "identifier": 'ACTION_162_play_sound_26',
        "command": 'play_sound',
        "args": [Sounds._033_JUMPING_BOUNCING_FISH, 4]
    },
    {
        "identifier": 'ACTION_162_jump_to_height_27',
        "command": 'jump_to_height',
        "args": [128]
    },
    {
        "identifier": 'ACTION_162_set_priority_28',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_162_walk_to_xy_coords_29',
        "command": 'walk_to_xy_coords',
        "args": [29, 72]
    },
    {
        "identifier": 'ACTION_162_object_memory_modify_bits_30',
        "command": 'object_memory_modify_bits',
        "args": [0x09, [5], [4, 6]]
    },
    {
        "identifier": 'ACTION_162_set_animation_speed_31',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_162_shift_northwest_steps_32',
        "command": 'shift_northwest_steps',
        "args": [9]
    },
    {
        "identifier": 'ACTION_162_set_animation_speed_33',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FASTER, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_162_shift_north_steps_34',
        "command": 'shift_north_steps',
        "args": [5]
    },
    {
        "identifier": 'ACTION_162_shift_northwest_steps_35',
        "command": 'shift_northwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_162_shift_north_steps_36',
        "command": 'shift_north_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_162_shift_northeast_steps_37',
        "command": 'shift_northeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_162_set_animation_speed_38',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_162_transfer_to_xyzf_39',
        "command": 'transfer_to_xyzf',
        "args": [24, 43, 0, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_162_visibility_on_40',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_162_face_southwest_41',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_162_pause_42',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_162_db_43',
        "command": 'db',
        "args": [0x3a, 0x00, 0x00, 0x03, 0x37, 0x20]
    },
    {
        "identifier": 'ACTION_162_jmp_44',
        "command": 'jmp',
        "args": ['ACTION_162_pause_42']
    },
    {
        "identifier": 'ACTION_162_set_bit_45',
        "command": 'set_bit',
        "args": [0x7078, 1]
    },
    {
        "identifier": 'ACTION_162_play_sound_46',
        "command": 'play_sound',
        "args": [Sounds._033_JUMPING_BOUNCING_FISH, 4]
    },
    {
        "identifier": 'ACTION_162_jump_to_height_47',
        "command": 'jump_to_height',
        "args": [128]
    },
    {
        "identifier": 'ACTION_162_walk_to_xy_coords_48',
        "command": 'walk_to_xy_coords',
        "args": [25, 36]
    },
    {
        "identifier": 'ACTION_162_set_animation_speed_49',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FASTER, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_162_shift_northwest_steps_50',
        "command": 'shift_northwest_steps',
        "args": [4]
    },
    {
        "identifier": 'ACTION_162_set_animation_speed_51',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_162_shift_northwest_steps_52',
        "command": 'shift_northwest_steps',
        "args": [4]
    },
    {
        "identifier": 'ACTION_162_set_animation_speed_53',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FASTER, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_162_shift_north_steps_54',
        "command": 'shift_north_steps',
        "args": [5]
    },
    {
        "identifier": 'ACTION_162_set_animation_speed_55',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_162_shift_northwest_steps_56',
        "command": 'shift_northwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_162_set_animation_speed_57',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_162_transfer_to_xyzf_58',
        "command": 'transfer_to_xyzf',
        "args": [20, 16, 0, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_162_visibility_on_59',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_162_face_southeast_60',
        "command": 'face_southeast'
    },
    {
        "identifier": 'ACTION_162_pause_61',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_162_db_62',
        "command": 'db',
        "args": [0x3a, 0x00, 0x00, 0x04, 0x65, 0x20]
    },
    {
        "identifier": 'ACTION_162_jmp_63',
        "command": 'jmp',
        "args": ['ACTION_162_pause_61']
    },
    {
        "identifier": 'ACTION_162_set_bit_64',
        "command": 'set_bit',
        "args": [0x7077, 2]
    },
    {
        "identifier": 'ACTION_162_play_sound_65',
        "command": 'play_sound',
        "args": [Sounds._033_JUMPING_BOUNCING_FISH, 4]
    },
    {
        "identifier": 'ACTION_162_jump_to_height_66',
        "command": 'jump_to_height',
        "args": [144]
    },
    {
        "identifier": 'ACTION_162_shift_northeast_steps_67',
        "command": 'shift_northeast_steps',
        "args": [5]
    },
    {
        "identifier": 'ACTION_162_visibility_off_68',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_162_ret_69',
        "command": 'ret'
    }
]
