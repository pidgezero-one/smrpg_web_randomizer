from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_48_object_memory_set_bit_0',
        "command": 'object_memory_set_bit',
        "args": [0x0b, [3]]
    },
    {
        "identifier": 'ACTION_48_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_48_shift_northeast_steps_2',
        "command": 'shift_northeast_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_48_pause_3',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_48_face_northwest_4',
        "command": 'face_northwest'
    },
    {
        "identifier": 'ACTION_48_pause_5',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_48_face_southeast_6',
        "command": 'face_southeast'
    },
    {
        "identifier": 'ACTION_48_pause_7',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_48_jmp_if_random_above_128_8',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_48_shift_southwest_steps_27']
    },
    {
        "identifier": 'ACTION_48_jump_to_height_silent_9',
        "command": 'jump_to_height_silent',
        "args": [108]
    },
    {
        "identifier": 'ACTION_48_shift_northeast_steps_10',
        "command": 'shift_northeast_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_48_pause_11',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_48_shift_northeast_steps_12',
        "command": 'shift_northeast_steps',
        "args": [4]
    },
    {
        "identifier": 'ACTION_48_shift_southeast_steps_13',
        "command": 'shift_southeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_48_shift_southwest_steps_14',
        "command": 'shift_southwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_48_pause_15',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_48_walk_1_step_northwest_16',
        "command": 'walk_1_step_northwest'
    },
    {
        "identifier": 'ACTION_48_shift_southwest_steps_17',
        "command": 'shift_southwest_steps',
        "args": [4]
    },
    {
        "identifier": 'ACTION_48_pause_18',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_48_jump_to_height_silent_19',
        "command": 'jump_to_height_silent',
        "args": [108]
    },
    {
        "identifier": 'ACTION_48_pause_20',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_48_shift_southwest_steps_21',
        "command": 'shift_southwest_steps',
        "args": [4]
    },
    {
        "identifier": 'ACTION_48_jump_to_height_silent_22',
        "command": 'jump_to_height_silent',
        "args": [108]
    },
    {
        "identifier": 'ACTION_48_pause_23',
        "command": 'pause',
        "args": [12]
    },
    {
        "identifier": 'ACTION_48_walk_1_step_northwest_24',
        "command": 'walk_1_step_northwest'
    },
    {
        "identifier": 'ACTION_48_pause_25',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_48_jmp_26',
        "command": 'jmp',
        "args": ['ACTION_48_object_memory_set_bit_0']
    },
    {
        "identifier": 'ACTION_48_shift_southwest_steps_27',
        "command": 'shift_southwest_steps',
        "args": [5]
    },
    {
        "identifier": 'ACTION_48_walk_1_step_southeast_28',
        "command": 'walk_1_step_southeast'
    },
    {
        "identifier": 'ACTION_48_pause_29',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_48_face_southwest_30',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_48_jump_to_height_silent_31',
        "command": 'jump_to_height_silent',
        "args": [108]
    },
    {
        "identifier": 'ACTION_48_pause_32',
        "command": 'pause',
        "args": [12]
    },
    {
        "identifier": 'ACTION_48_walk_1_step_southwest_33',
        "command": 'walk_1_step_southwest'
    },
    {
        "identifier": 'ACTION_48_pause_34',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_48_shift_southwest_steps_35',
        "command": 'shift_southwest_steps',
        "args": [5]
    },
    {
        "identifier": 'ACTION_48_face_northwest_36',
        "command": 'face_northwest'
    },
    {
        "identifier": 'ACTION_48_jump_to_height_silent_37',
        "command": 'jump_to_height_silent',
        "args": [108]
    },
    {
        "identifier": 'ACTION_48_pause_38',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'ACTION_48_jmp_if_random_above_128_39',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_48_pause_52']
    },
    {
        "identifier": 'ACTION_48_shift_northeast_steps_40',
        "command": 'shift_northeast_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_48_face_northwest_41',
        "command": 'face_northwest'
    },
    {
        "identifier": 'ACTION_48_jump_to_height_silent_42',
        "command": 'jump_to_height_silent',
        "args": [72]
    },
    {
        "identifier": 'ACTION_48_pause_43',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_48_walk_1_step_northwest_44',
        "command": 'walk_1_step_northwest'
    },
    {
        "identifier": 'ACTION_48_shift_northeast_steps_45',
        "command": 'shift_northeast_steps',
        "args": [4]
    },
    {
        "identifier": 'ACTION_48_pause_46',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_48_jump_to_height_silent_47',
        "command": 'jump_to_height_silent',
        "args": [72]
    },
    {
        "identifier": 'ACTION_48_pause_48',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_48_walk_1_step_northeast_49',
        "command": 'walk_1_step_northeast'
    },
    {
        "identifier": 'ACTION_48_pause_50',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_48_jmp_51',
        "command": 'jmp',
        "args": ['ACTION_48_object_memory_set_bit_0']
    },
    {
        "identifier": 'ACTION_48_pause_52',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_48_jump_to_height_silent_53',
        "command": 'jump_to_height_silent',
        "args": [108]
    },
    {
        "identifier": 'ACTION_48_pause_54',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'ACTION_48_walk_1_step_southeast_55',
        "command": 'walk_1_step_southeast'
    },
    {
        "identifier": 'ACTION_48_walk_1_step_southwest_56',
        "command": 'walk_1_step_southwest'
    },
    {
        "identifier": 'ACTION_48_walk_1_step_northwest_57',
        "command": 'walk_1_step_northwest'
    },
    {
        "identifier": 'ACTION_48_shift_northeast_steps_58',
        "command": 'shift_northeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_48_shift_northwest_steps_59',
        "command": 'shift_northwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_48_face_northeast_60',
        "command": 'face_northeast'
    },
    {
        "identifier": 'ACTION_48_jump_to_height_silent_61',
        "command": 'jump_to_height_silent',
        "args": [72]
    },
    {
        "identifier": 'ACTION_48_pause_62',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_48_walk_1_step_northeast_63',
        "command": 'walk_1_step_northeast'
    },
    {
        "identifier": 'ACTION_48_pause_64',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'ACTION_48_walk_1_step_southeast_65',
        "command": 'walk_1_step_southeast'
    },
    {
        "identifier": 'ACTION_48_shift_northeast_steps_66',
        "command": 'shift_northeast_steps',
        "args": [4]
    },
    {
        "identifier": 'ACTION_48_pause_67',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_48_jump_to_height_silent_68',
        "command": 'jump_to_height_silent',
        "args": [88]
    },
    {
        "identifier": 'ACTION_48_shift_northeast_steps_69',
        "command": 'shift_northeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_48_pause_70',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_48_jmp_71',
        "command": 'jmp',
        "args": ['ACTION_48_object_memory_set_bit_0']
    }
]
