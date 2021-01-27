from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_643_sequence_looping_on_0',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_643_set_priority_1',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_643_set_animation_speed_2',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_643_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x7078, 3, 'ACTION_643_shift_southeast_steps_24']
    },
    {
        "identifier": 'ACTION_643_pause_4',
        "command": 'pause',
        "args": [173]
    },
    {
        "identifier": 'ACTION_643_start_loop_n_times_5',
        "command": 'start_loop_n_times',
        "args": [4]
    },
    {
        "identifier": 'ACTION_643_shift_southeast_steps_6',
        "command": 'shift_southeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_643_shift_northwest_steps_7',
        "command": 'shift_northwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_643_end_loop_8',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_643_start_loop_n_times_9',
        "command": 'start_loop_n_times',
        "args": [3]
    },
    {
        "identifier": 'ACTION_643_turn_clockwise_45_degrees_n_times_10',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [6]
    },
    {
        "identifier": 'ACTION_643_pause_11',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'ACTION_643_end_loop_12',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_643_shift_southeast_steps_13',
        "command": 'shift_southeast_steps',
        "args": [6]
    },
    {
        "identifier": 'ACTION_643_jump_to_height_14',
        "command": 'jump_to_height',
        "args": [120]
    },
    {
        "identifier": 'ACTION_643_set_animation_speed_15',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_643_fixed_f_coord_on_16',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_643_set_sprite_sequence_17',
        "command": 'set_sprite_sequence',
        "args": [2, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_643_shift_northeast_steps_18',
        "command": 'shift_northeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_643_pause_19',
        "command": 'pause',
        "args": [7]
    },
    {
        "identifier": 'ACTION_643_floating_off_20',
        "command": 'floating_off'
    },
    {
        "identifier": 'ACTION_643_set_sprite_sequence_21',
        "command": 'set_sprite_sequence',
        "args": [3, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_643_set_bit_22',
        "command": 'set_bit',
        "args": [0x7043, 3]
    },
    {
        "identifier": 'ACTION_643_ret_23',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_643_shift_southeast_steps_24',
        "command": 'shift_southeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_643_shift_northwest_steps_25',
        "command": 'shift_northwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_643_jmp_26',
        "command": 'jmp',
        "args": ['ACTION_643_shift_southeast_steps_24']
    }
]
