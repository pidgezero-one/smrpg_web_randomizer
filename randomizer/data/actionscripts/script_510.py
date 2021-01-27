from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_510_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x704b, 6, 'ACTION_510_set_animation_speed_42']
    },
    {
        "identifier": 'ACTION_510_reset_properties_1',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_510_set_700C_to_object_coord_2',
        "command": 'set_700C_to_object_coord',
        "args": [AreaObjects.MARIO, Coords.F, []]
    },
    {
        "identifier": 'ACTION_510_jmp_if_700C_equals_short_3',
        "command": 'jmp_if_700C_equals_short',
        "args": [0, 'ACTION_510_start_loop_n_times_14']
    },
    {
        "identifier": 'ACTION_510_jmp_if_700C_equals_short_4',
        "command": 'jmp_if_700C_equals_short',
        "args": [1, 'ACTION_510_turn_clockwise_45_degrees_n_times_11']
    },
    {
        "identifier": 'ACTION_510_jmp_if_700C_equals_short_5',
        "command": 'jmp_if_700C_equals_short',
        "args": [2, 'ACTION_510_start_loop_n_times_38']
    },
    {
        "identifier": 'ACTION_510_jmp_if_700C_equals_short_6',
        "command": 'jmp_if_700C_equals_short',
        "args": [3, 'ACTION_510_start_loop_n_times_35']
    },
    {
        "identifier": 'ACTION_510_jmp_if_700C_equals_short_7',
        "command": 'jmp_if_700C_equals_short',
        "args": [4, 'ACTION_510_start_loop_n_times_31']
    },
    {
        "identifier": 'ACTION_510_jmp_if_700C_equals_short_8',
        "command": 'jmp_if_700C_equals_short',
        "args": [5, 'ACTION_510_start_loop_n_times_27']
    },
    {
        "identifier": 'ACTION_510_jmp_if_700C_equals_short_9',
        "command": 'jmp_if_700C_equals_short',
        "args": [6, 'ACTION_510_start_loop_n_times_23']
    },
    {
        "identifier": 'ACTION_510_jmp_if_700C_equals_short_10',
        "command": 'jmp_if_700C_equals_short',
        "args": [7, 'ACTION_510_start_loop_n_times_19']
    },
    {
        "identifier": 'ACTION_510_turn_clockwise_45_degrees_n_times_11',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [1]
    },
    {
        "identifier": 'ACTION_510_pause_12',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_510_jmp_13',
        "command": 'jmp',
        "args": ['ACTION_510_start_loop_n_times_38']
    },
    {
        "identifier": 'ACTION_510_start_loop_n_times_14',
        "command": 'start_loop_n_times',
        "args": [1]
    },
    {
        "identifier": 'ACTION_510_turn_clockwise_45_degrees_n_times_15',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [1]
    },
    {
        "identifier": 'ACTION_510_pause_16',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_510_end_loop_17',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_510_jmp_18',
        "command": 'jmp',
        "args": ['ACTION_510_start_loop_n_times_38']
    },
    {
        "identifier": 'ACTION_510_start_loop_n_times_19',
        "command": 'start_loop_n_times',
        "args": [2]
    },
    {
        "identifier": 'ACTION_510_turn_clockwise_45_degrees_n_times_20',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [1]
    },
    {
        "identifier": 'ACTION_510_pause_21',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_510_jmp_22',
        "command": 'jmp',
        "args": ['ACTION_510_start_loop_n_times_38']
    },
    {
        "identifier": 'ACTION_510_start_loop_n_times_23',
        "command": 'start_loop_n_times',
        "args": [3]
    },
    {
        "identifier": 'ACTION_510_turn_clockwise_45_degrees_n_times_24',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [1]
    },
    {
        "identifier": 'ACTION_510_pause_25',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_510_jmp_26',
        "command": 'jmp',
        "args": ['ACTION_510_start_loop_n_times_38']
    },
    {
        "identifier": 'ACTION_510_start_loop_n_times_27',
        "command": 'start_loop_n_times',
        "args": [4]
    },
    {
        "identifier": 'ACTION_510_turn_clockwise_45_degrees_n_times_28',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [1]
    },
    {
        "identifier": 'ACTION_510_pause_29',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_510_jmp_30',
        "command": 'jmp',
        "args": ['ACTION_510_start_loop_n_times_38']
    },
    {
        "identifier": 'ACTION_510_start_loop_n_times_31',
        "command": 'start_loop_n_times',
        "args": [5]
    },
    {
        "identifier": 'ACTION_510_turn_clockwise_45_degrees_n_times_32',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [1]
    },
    {
        "identifier": 'ACTION_510_pause_33',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_510_jmp_34',
        "command": 'jmp',
        "args": ['ACTION_510_start_loop_n_times_38']
    },
    {
        "identifier": 'ACTION_510_start_loop_n_times_35',
        "command": 'start_loop_n_times',
        "args": [6]
    },
    {
        "identifier": 'ACTION_510_turn_clockwise_45_degrees_n_times_36',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [1]
    },
    {
        "identifier": 'ACTION_510_pause_37',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_510_start_loop_n_times_38',
        "command": 'start_loop_n_times',
        "args": [6]
    },
    {
        "identifier": 'ACTION_510_turn_clockwise_45_degrees_n_times_39',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [1]
    },
    {
        "identifier": 'ACTION_510_pause_40',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_510_end_loop_41',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_510_set_animation_speed_42',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_510_set_sprite_sequence_43',
        "command": 'set_sprite_sequence',
        "args": [10, 2, [_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_510_pause_44',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'ACTION_510_set_animation_speed_45',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_510_pause_46',
        "command": 'pause',
        "args": [40]
    },
    {
        "identifier": 'ACTION_510_set_sprite_sequence_47',
        "command": 'set_sprite_sequence',
        "args": [30, 2, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_510_pause_48',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'ACTION_510_reset_properties_49',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_510_clear_bit_50',
        "command": 'clear_bit',
        "args": [0x704b, 6]
    },
    {
        "identifier": 'ACTION_510_ret_51',
        "command": 'ret'
    }
]
