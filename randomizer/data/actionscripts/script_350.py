from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_350_visibility_off_0',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_350_object_memory_set_bit_1',
        "command": 'object_memory_set_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_350_set_animation_speed_2',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_350_clear_solidity_bits_3',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_350_set_700C_to_pressed_button_4',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_350_mem_700C_and_const_5',
        "command": 'mem_700C_and_const',
        "args": [0x0007]
    },
    {
        "identifier": 'ACTION_350_jmp_if_700C_equals_short_6',
        "command": 'jmp_if_700C_equals_short',
        "args": [0, 'ACTION_350_create_packet_at_object_coords_jmp_if_null_20']
    },
    {
        "identifier": 'ACTION_350_jmp_if_700C_equals_short_7',
        "command": 'jmp_if_700C_equals_short',
        "args": [1, 'ACTION_350_pause_19']
    },
    {
        "identifier": 'ACTION_350_jmp_if_700C_equals_short_8',
        "command": 'jmp_if_700C_equals_short',
        "args": [2, 'ACTION_350_pause_18']
    },
    {
        "identifier": 'ACTION_350_jmp_if_700C_equals_short_9',
        "command": 'jmp_if_700C_equals_short',
        "args": [3, 'ACTION_350_pause_17']
    },
    {
        "identifier": 'ACTION_350_jmp_if_700C_equals_short_10',
        "command": 'jmp_if_700C_equals_short',
        "args": [4, 'ACTION_350_pause_16']
    },
    {
        "identifier": 'ACTION_350_jmp_if_700C_equals_short_11',
        "command": 'jmp_if_700C_equals_short',
        "args": [5, 'ACTION_350_pause_15']
    },
    {
        "identifier": 'ACTION_350_jmp_if_700C_equals_short_12',
        "command": 'jmp_if_700C_equals_short',
        "args": [6, 'ACTION_350_pause_14']
    },
    {
        "identifier": 'ACTION_350_pause_13',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'ACTION_350_pause_14',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'ACTION_350_pause_15',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'ACTION_350_pause_16',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'ACTION_350_pause_17',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'ACTION_350_pause_18',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'ACTION_350_pause_19',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'ACTION_350_create_packet_at_object_coords_jmp_if_null_20',
        "command": 'create_packet_at_object_coords_jmp_if_null',
        "args": [NPCPackets._024_BOMB_EXPLOSION_SFX, AreaObjects.DUMMY_0X07, 'ACTION_350_visibility_on_21']
    },
    {
        "identifier": 'ACTION_350_visibility_on_21',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_350_object_memory_clear_bit_22',
        "command": 'object_memory_clear_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_350_set_solidity_bits_23',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_350_start_loop_n_times_24',
        "command": 'start_loop_n_times',
        "args": [7]
    },
    {
        "identifier": 'ACTION_350_walk_1_step_f_direction_25',
        "command": 'walk_1_step_f_direction'
    },
    {
        "identifier": 'ACTION_350_shadow_on_26',
        "command": 'shadow_on'
    },
    {
        "identifier": 'ACTION_350_end_loop_27',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_350_visibility_off_28',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_350_object_memory_set_bit_29',
        "command": 'object_memory_set_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_350_clear_solidity_bits_30',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_350_pause_31',
        "command": 'pause',
        "args": [128]
    },
    {
        "identifier": 'ACTION_350_set_700C_to_pressed_button_32',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_350_jmp_if_700C_equals_short_33',
        "command": 'jmp_if_700C_equals_short',
        "args": [26, 'ACTION_350_transfer_to_xyzf_39']
    },
    {
        "identifier": 'ACTION_350_jmp_if_700C_equals_short_34',
        "command": 'jmp_if_700C_equals_short',
        "args": [27, 'ACTION_350_transfer_to_xyzf_41']
    },
    {
        "identifier": 'ACTION_350_jmp_if_700C_equals_short_35',
        "command": 'jmp_if_700C_equals_short',
        "args": [28, 'ACTION_350_transfer_to_xyzf_43']
    },
    {
        "identifier": 'ACTION_350_jmp_if_700C_equals_short_36',
        "command": 'jmp_if_700C_equals_short',
        "args": [29, 'ACTION_350_transfer_to_xyzf_45']
    },
    {
        "identifier": 'ACTION_350_jmp_if_700C_equals_short_37',
        "command": 'jmp_if_700C_equals_short',
        "args": [30, 'ACTION_350_transfer_to_xyzf_47']
    },
    {
        "identifier": 'ACTION_350_jmp_if_700C_equals_short_38',
        "command": 'jmp_if_700C_equals_short',
        "args": [31, 'ACTION_350_transfer_to_xyzf_49']
    },
    {
        "identifier": 'ACTION_350_transfer_to_xyzf_39',
        "command": 'transfer_to_xyzf',
        "args": [23, 59, 10, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_350_jmp_40',
        "command": 'jmp',
        "args": ['ACTION_350_create_packet_at_object_coords_jmp_if_null_20']
    },
    {
        "identifier": 'ACTION_350_transfer_to_xyzf_41',
        "command": 'transfer_to_xyzf',
        "args": [21, 63, 10, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_350_jmp_42',
        "command": 'jmp',
        "args": ['ACTION_350_create_packet_at_object_coords_jmp_if_null_20']
    },
    {
        "identifier": 'ACTION_350_transfer_to_xyzf_43',
        "command": 'transfer_to_xyzf',
        "args": [30, 63, 10, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_350_jmp_44',
        "command": 'jmp',
        "args": ['ACTION_350_create_packet_at_object_coords_jmp_if_null_20']
    },
    {
        "identifier": 'ACTION_350_transfer_to_xyzf_45',
        "command": 'transfer_to_xyzf',
        "args": [28, 59, 10, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_350_jmp_46',
        "command": 'jmp',
        "args": ['ACTION_350_create_packet_at_object_coords_jmp_if_null_20']
    },
    {
        "identifier": 'ACTION_350_transfer_to_xyzf_47',
        "command": 'transfer_to_xyzf',
        "args": [22, 61, 10, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_350_jmp_48',
        "command": 'jmp',
        "args": ['ACTION_350_create_packet_at_object_coords_jmp_if_null_20']
    },
    {
        "identifier": 'ACTION_350_transfer_to_xyzf_49',
        "command": 'transfer_to_xyzf',
        "args": [29, 61, 10, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_350_jmp_50',
        "command": 'jmp',
        "args": ['ACTION_350_create_packet_at_object_coords_jmp_if_null_20']
    }
]
