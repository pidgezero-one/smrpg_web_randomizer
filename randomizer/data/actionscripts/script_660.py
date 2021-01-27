from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_660_set_700C_to_current_level_0',
        "command": 'set_700C_to_current_level'
    },
    {
        "identifier": 'ACTION_660_jmp_if_700C_equals_short_1',
        "command": 'jmp_if_700C_equals_short',
        "args": [378, 'ACTION_660_shadow_off_9']
    },
    {
        "identifier": 'ACTION_660_jmp_if_700C_equals_short_2',
        "command": 'jmp_if_700C_equals_short',
        "args": [381, 'ACTION_660_shadow_off_9']
    },
    {
        "identifier": 'ACTION_660_set_animation_speed_3',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_660_shift_z_up_steps_4',
        "command": 'shift_z_up_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_660_pause_5',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_660_shift_z_down_steps_6',
        "command": 'shift_z_down_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_660_pause_7',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_660_jmp_8',
        "command": 'jmp',
        "args": ['ACTION_660_set_700C_to_current_level_0']
    },
    {
        "identifier": 'ACTION_660_shadow_off_9',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_660_set_animation_speed_10',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_660_sequence_looping_on_11',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_660_shift_z_up_steps_12',
        "command": 'shift_z_up_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_660_jmp_if_random_above_128_13',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_660_shift_z_up_steps_15']
    },
    {
        "identifier": 'ACTION_660_jump_to_subroutine_14',
        "command": 'jump_to_subroutine',
        "args": [0x78cb]
    },
    {
        "identifier": 'ACTION_660_shift_z_up_steps_15',
        "command": 'shift_z_up_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_660_jmp_if_random_above_128_16',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_660_shift_z_down_steps_18']
    },
    {
        "identifier": 'ACTION_660_jump_to_subroutine_17',
        "command": 'jump_to_subroutine',
        "args": [0x78cb]
    },
    {
        "identifier": 'ACTION_660_shift_z_down_steps_18',
        "command": 'shift_z_down_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_660_jmp_if_random_above_128_19',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_660_shift_z_down_steps_21']
    },
    {
        "identifier": 'ACTION_660_jump_to_subroutine_20',
        "command": 'jump_to_subroutine',
        "args": [0x78cb]
    },
    {
        "identifier": 'ACTION_660_shift_z_down_steps_21',
        "command": 'shift_z_down_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_660_jmp_if_random_above_128_22',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_660_shadow_off_9']
    },
    {
        "identifier": 'ACTION_660_jump_to_subroutine_23',
        "command": 'jump_to_subroutine',
        "args": [0x78cb]
    },
    {
        "identifier": 'ACTION_660_jmp_24',
        "command": 'jmp',
        "args": ['ACTION_660_shadow_off_9']
    },
    {
        "identifier": 'ACTION_660_set_700C_to_object_coord_25',
        "command": 'set_700C_to_object_coord',
        "args": [AreaObjects.DUMMY_0X07, Coords.F, []]
    },
    {
        "identifier": 'ACTION_660_pause_26',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_660_turn_random_direction_27',
        "command": 'turn_random_direction'
    },
    {
        "identifier": 'ACTION_660_pause_28',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_660_turn_random_direction_29',
        "command": 'turn_random_direction'
    },
    {
        "identifier": 'ACTION_660_pause_30',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_660_face_east_7C_31',
        "command": 'face_east_7C'
    },
    {
        "identifier": 'ACTION_660_ret_32',
        "command": 'ret'
    }
]
