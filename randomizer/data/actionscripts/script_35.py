from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_35_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 5, 'ACTION_35_jmp_if_bit_set_3']
    },
    {
        "identifier": 'ACTION_35_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 6, 'ACTION_35_face_southwest_31']
    },
    {
        "identifier": 'ACTION_35_jmp_2',
        "command": 'jmp',
        "args": ['ACTION_35_face_southwest_21']
    },
    {
        "identifier": 'ACTION_35_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 6, 'ACTION_35_face_southwest_11']
    },
    {
        "identifier": 'ACTION_35_face_northeast_4',
        "command": 'face_northeast'
    },
    {
        "identifier": 'ACTION_35_jump_to_subroutine_5',
        "command": 'jump_to_subroutine',
        "args": [0x0cc4]
    },
    {
        "identifier": 'ACTION_35_set_priority_6',
        "command": 'set_priority',
        "args": [2]
    },
    {
        "identifier": 'ACTION_35_shift_northeast_steps_7',
        "command": 'shift_northeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_35_set_priority_8',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_35_shift_northeast_steps_9',
        "command": 'shift_northeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_35_jmp_10',
        "command": 'jmp',
        "args": ['ACTION_32_shift_z_up_steps_20']
    },
    {
        "identifier": 'ACTION_35_face_southwest_11',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_35_jump_to_subroutine_12',
        "command": 'jump_to_subroutine',
        "args": [0x0cc4]
    },
    {
        "identifier": 'ACTION_35_set_priority_13',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_35_walk_1_step_southwest_14',
        "command": 'walk_1_step_southwest'
    },
    {
        "identifier": 'ACTION_35_walk_1_step_southeast_15',
        "command": 'walk_1_step_southeast'
    },
    {
        "identifier": 'ACTION_35_shift_northeast_steps_16',
        "command": 'shift_northeast_steps',
        "args": [10]
    },
    {
        "identifier": 'ACTION_35_set_priority_17',
        "command": 'set_priority',
        "args": [2]
    },
    {
        "identifier": 'ACTION_35_walk_1_step_northwest_18',
        "command": 'walk_1_step_northwest'
    },
    {
        "identifier": 'ACTION_35_walk_1_step_southwest_19',
        "command": 'walk_1_step_southwest'
    },
    {
        "identifier": 'ACTION_35_jmp_20',
        "command": 'jmp',
        "args": ['ACTION_32_shift_z_up_steps_20']
    },
    {
        "identifier": 'ACTION_35_face_southwest_21',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_35_jump_to_subroutine_22',
        "command": 'jump_to_subroutine',
        "args": [0x0cc4]
    },
    {
        "identifier": 'ACTION_35_set_priority_23',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_35_walk_1_step_southwest_24',
        "command": 'walk_1_step_southwest'
    },
    {
        "identifier": 'ACTION_35_walk_1_step_northwest_25',
        "command": 'walk_1_step_northwest'
    },
    {
        "identifier": 'ACTION_35_set_priority_26',
        "command": 'set_priority',
        "args": [2]
    },
    {
        "identifier": 'ACTION_35_shift_northeast_steps_27',
        "command": 'shift_northeast_steps',
        "args": [10]
    },
    {
        "identifier": 'ACTION_35_walk_1_step_southeast_28',
        "command": 'walk_1_step_southeast'
    },
    {
        "identifier": 'ACTION_35_walk_1_step_southwest_29',
        "command": 'walk_1_step_southwest'
    },
    {
        "identifier": 'ACTION_35_jmp_30',
        "command": 'jmp',
        "args": ['ACTION_32_shift_z_up_steps_20']
    },
    {
        "identifier": 'ACTION_35_face_southwest_31',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_35_jump_to_subroutine_32',
        "command": 'jump_to_subroutine',
        "args": [0x0cc4]
    },
    {
        "identifier": 'ACTION_35_set_priority_33',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_35_walk_1_step_southwest_34',
        "command": 'walk_1_step_southwest'
    },
    {
        "identifier": 'ACTION_35_walk_1_step_southeast_35',
        "command": 'walk_1_step_southeast'
    },
    {
        "identifier": 'ACTION_35_shift_northeast_steps_36',
        "command": 'shift_northeast_steps',
        "args": [10]
    },
    {
        "identifier": 'ACTION_35_walk_1_step_southeast_37',
        "command": 'walk_1_step_southeast'
    },
    {
        "identifier": 'ACTION_35_shift_southwest_steps_38',
        "command": 'shift_southwest_steps',
        "args": [5]
    },
    {
        "identifier": 'ACTION_35_set_priority_39',
        "command": 'set_priority',
        "args": [2]
    },
    {
        "identifier": 'ACTION_35_start_loop_n_times_40',
        "command": 'start_loop_n_times',
        "args": [2]
    },
    {
        "identifier": 'ACTION_35_walk_1_step_northwest_41',
        "command": 'walk_1_step_northwest'
    },
    {
        "identifier": 'ACTION_35_walk_1_step_southwest_42',
        "command": 'walk_1_step_southwest'
    },
    {
        "identifier": 'ACTION_35_end_loop_43',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_35_shift_southwest_steps_44',
        "command": 'shift_southwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_35_set_priority_45',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_35_walk_1_step_southeast_46',
        "command": 'walk_1_step_southeast'
    },
    {
        "identifier": 'ACTION_35_walk_1_step_northeast_47',
        "command": 'walk_1_step_northeast'
    },
    {
        "identifier": 'ACTION_35_jmp_48',
        "command": 'jmp',
        "args": ['ACTION_32_shift_z_up_steps_20']
    }
]
