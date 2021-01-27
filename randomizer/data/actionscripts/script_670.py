from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_670_set_700C_to_object_coord_0',
        "command": 'set_700C_to_object_coord',
        "args": [AreaObjects.MARIO, Coords.F, []]
    },
    {
        "identifier": 'ACTION_670_set_7000_short_mem_to_700C_1',
        "command": 'set_7000_short_mem_to_700C',
        "args": [0x7038]
    },
    {
        "identifier": 'ACTION_670_jmp_if_var_equals_short_2',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7038, 1, 'ACTION_670_start_loop_n_times_15']
    },
    {
        "identifier": 'ACTION_670_jmp_if_var_equals_short_3',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7038, 3, 'ACTION_670_start_loop_n_times_22']
    },
    {
        "identifier": 'ACTION_670_jmp_if_var_equals_short_4',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7038, 5, 'ACTION_670_start_loop_n_times_29']
    },
    {
        "identifier": 'ACTION_670_jmp_if_var_equals_short_5',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7038, 7, 'ACTION_670_start_loop_n_times_36']
    },
    {
        "identifier": 'ACTION_670_set_700C_to_70A0_short_mem_6',
        "command": 'set_700C_to_70A0_short_mem',
        "args": [0x70ae]
    },
    {
        "identifier": 'ACTION_670_set_70A0_short_mem_to_700C_7',
        "command": 'set_70A0_short_mem_to_700C',
        "args": [0x70ab]
    },
    {
        "identifier": 'ACTION_670_db_8',
        "command": 'db',
        "args": [0xfd, 0x24, 0x00, 0x13]
    },
    {
        "identifier": 'ACTION_670_set_7000_short_mem_to_700C_9',
        "command": 'set_7000_short_mem_to_700C',
        "args": [0x7000]
    },
    {
        "identifier": 'ACTION_670_mem_700C_and_const_10',
        "command": 'mem_700C_and_const',
        "args": [0x00c0]
    },
    {
        "identifier": 'ACTION_670_jmp_if_700C_equals_short_11',
        "command": 'jmp_if_700C_equals_short',
        "args": [0, 'ACTION_670_start_loop_n_times_15']
    },
    {
        "identifier": 'ACTION_670_jmp_if_700C_equals_short_12',
        "command": 'jmp_if_700C_equals_short',
        "args": [64, 'ACTION_670_start_loop_n_times_22']
    },
    {
        "identifier": 'ACTION_670_jmp_if_700C_equals_short_13',
        "command": 'jmp_if_700C_equals_short',
        "args": [128, 'ACTION_670_start_loop_n_times_29']
    },
    {
        "identifier": 'ACTION_670_jmp_if_700C_equals_short_14',
        "command": 'jmp_if_700C_equals_short',
        "args": [192, 'ACTION_670_start_loop_n_times_36']
    },
    {
        "identifier": 'ACTION_670_start_loop_n_times_15',
        "command": 'start_loop_n_times',
        "args": [2]
    },
    {
        "identifier": 'ACTION_670_set_sprite_sequence_16',
        "command": 'set_sprite_sequence',
        "args": [6, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_670_pause_17',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'ACTION_670_set_sprite_sequence_18',
        "command": 'set_sprite_sequence',
        "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_670_pause_19',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'ACTION_670_end_loop_20',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_670_jmp_21',
        "command": 'jmp',
        "args": ['ACTION_670_reset_properties_42']
    },
    {
        "identifier": 'ACTION_670_start_loop_n_times_22',
        "command": 'start_loop_n_times',
        "args": [2]
    },
    {
        "identifier": 'ACTION_670_set_sprite_sequence_23',
        "command": 'set_sprite_sequence',
        "args": [6, 0, [_0x08Flags.READ_AS_MOLD]]
    },
    {
        "identifier": 'ACTION_670_pause_24',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'ACTION_670_set_sprite_sequence_25',
        "command": 'set_sprite_sequence',
        "args": [0, 0, [_0x08Flags.READ_AS_MOLD]]
    },
    {
        "identifier": 'ACTION_670_pause_26',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'ACTION_670_end_loop_27',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_670_jmp_28',
        "command": 'jmp',
        "args": ['ACTION_670_reset_properties_42']
    },
    {
        "identifier": 'ACTION_670_start_loop_n_times_29',
        "command": 'start_loop_n_times',
        "args": [2]
    },
    {
        "identifier": 'ACTION_670_set_sprite_sequence_30',
        "command": 'set_sprite_sequence',
        "args": [3, 0, [_0x08Flags.READ_AS_MOLD]]
    },
    {
        "identifier": 'ACTION_670_pause_31',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'ACTION_670_set_sprite_sequence_32',
        "command": 'set_sprite_sequence',
        "args": [7, 0, [_0x08Flags.READ_AS_MOLD]]
    },
    {
        "identifier": 'ACTION_670_pause_33',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'ACTION_670_end_loop_34',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_670_jmp_35',
        "command": 'jmp',
        "args": ['ACTION_670_reset_properties_42']
    },
    {
        "identifier": 'ACTION_670_start_loop_n_times_36',
        "command": 'start_loop_n_times',
        "args": [2]
    },
    {
        "identifier": 'ACTION_670_set_sprite_sequence_37',
        "command": 'set_sprite_sequence',
        "args": [3, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_670_pause_38',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'ACTION_670_set_sprite_sequence_39',
        "command": 'set_sprite_sequence',
        "args": [7, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_670_pause_40',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'ACTION_670_end_loop_41',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_670_reset_properties_42',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_670_set_700C_to_7000_short_mem_43',
        "command": 'set_700C_to_7000_short_mem',
        "args": [0x7038]
    },
    {
        "identifier": 'ACTION_670_face_east_7C_44',
        "command": 'face_east_7C'
    },
    {
        "identifier": 'ACTION_670_clear_bit_45',
        "command": 'clear_bit',
        "args": [0x7044, 7]
    },
    {
        "identifier": 'ACTION_670_ret_46',
        "command": 'ret'
    }
]
