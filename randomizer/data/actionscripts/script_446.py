from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_446_object_memory_set_bit_0',
        "command": 'object_memory_set_bit',
        "args": [0x3c, [6]]
    },
    {
        "identifier": 'ACTION_446_clear_solidity_bits_1',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS, _0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_446_floating_off_2',
        "command": 'floating_off'
    },
    {
        "identifier": 'ACTION_446_transfer_to_object_xy_3',
        "command": 'transfer_to_object_xy',
        "args": [AreaObjects.MARIO]
    },
    {
        "identifier": 'ACTION_446_jmp_if_bit_set_4',
        "command": 'jmp_if_bit_set',
        "args": [0x707c, 2, 'ACTION_446_visibility_off_31']
    },
    {
        "identifier": 'ACTION_446_jmp_if_bit_set_5',
        "command": 'jmp_if_bit_set',
        "args": [0x707c, 3, 'ACTION_446_visibility_off_31']
    },
    {
        "identifier": 'ACTION_446_jmp_if_random_above_128_6',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_446_shift_xy_pixels_9']
    },
    {
        "identifier": 'ACTION_446_shift_xy_pixels_7',
        "command": 'shift_xy_pixels',
        "args": [252, 4]
    },
    {
        "identifier": 'ACTION_446_jmp_8',
        "command": 'jmp',
        "args": ['ACTION_446_sequence_looping_on_10']
    },
    {
        "identifier": 'ACTION_446_shift_xy_pixels_9',
        "command": 'shift_xy_pixels',
        "args": [4, 252]
    },
    {
        "identifier": 'ACTION_446_sequence_looping_on_10',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_446_set_sprite_sequence_11',
        "command": 'set_sprite_sequence',
        "args": [0, 0, [_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_446_start_loop_n_times_12',
        "command": 'start_loop_n_times',
        "args": [5]
    },
    {
        "identifier": 'ACTION_446_jmp_if_bit_set_13',
        "command": 'jmp_if_bit_set',
        "args": [0x707c, 2, 'ACTION_446_visibility_off_31']
    },
    {
        "identifier": 'ACTION_446_jmp_if_bit_set_14',
        "command": 'jmp_if_bit_set',
        "args": [0x707c, 3, 'ACTION_446_visibility_off_31']
    },
    {
        "identifier": 'ACTION_446_pause_15',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_446_end_loop_16',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_446_jmp_if_bit_clear_17',
        "command": 'jmp_if_bit_clear',
        "args": [0x7076, 0, 'ACTION_446_start_loop_n_times_19']
    },
    {
        "identifier": 'ACTION_446_create_packet_at_object_coords_jmp_if_null_18',
        "command": 'create_packet_at_object_coords_jmp_if_null',
        "args": [NPCPackets._023_SPARKLES_MOVE_W, AreaObjects.MARIO, 'ACTION_446_start_loop_n_times_19']
    },
    {
        "identifier": 'ACTION_446_start_loop_n_times_19',
        "command": 'start_loop_n_times',
        "args": [5]
    },
    {
        "identifier": 'ACTION_446_jmp_if_bit_set_20',
        "command": 'jmp_if_bit_set',
        "args": [0x707c, 2, 'ACTION_446_visibility_off_31']
    },
    {
        "identifier": 'ACTION_446_jmp_if_bit_set_21',
        "command": 'jmp_if_bit_set',
        "args": [0x707c, 3, 'ACTION_446_visibility_off_31']
    },
    {
        "identifier": 'ACTION_446_pause_22',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_446_end_loop_23',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_446_jmp_if_bit_clear_24',
        "command": 'jmp_if_bit_clear',
        "args": [0x7076, 0, 'ACTION_446_start_loop_n_times_26']
    },
    {
        "identifier": 'ACTION_446_create_packet_at_object_coords_jmp_if_null_25',
        "command": 'create_packet_at_object_coords_jmp_if_null',
        "args": [NPCPackets._022_SPARKLES_MOVE_N, AreaObjects.MARIO, 'ACTION_446_start_loop_n_times_26']
    },
    {
        "identifier": 'ACTION_446_start_loop_n_times_26',
        "command": 'start_loop_n_times',
        "args": [11]
    },
    {
        "identifier": 'ACTION_446_jmp_if_bit_set_27',
        "command": 'jmp_if_bit_set',
        "args": [0x707c, 2, 'ACTION_446_visibility_off_31']
    },
    {
        "identifier": 'ACTION_446_jmp_if_bit_set_28',
        "command": 'jmp_if_bit_set',
        "args": [0x707c, 3, 'ACTION_446_visibility_off_31']
    },
    {
        "identifier": 'ACTION_446_pause_29',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_446_end_loop_30',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_446_visibility_off_31',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_446_ret_32',
        "command": 'ret'
    }
]
