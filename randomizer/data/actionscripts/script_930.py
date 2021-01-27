from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_930_fixed_f_coord_on_0',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_930_set_700C_to_object_coord_1',
        "command": 'set_700C_to_object_coord',
        "args": [AreaObjects.DUMMY_0X07, Coords.F, []]
    },
    {
        "identifier": 'ACTION_930_jmp_if_700C_equals_short_2',
        "command": 'jmp_if_700C_equals_short',
        "args": [1, 'ACTION_930_set_sprite_sequence_5']
    },
    {
        "identifier": 'ACTION_930_set_sprite_sequence_3',
        "command": 'set_sprite_sequence',
        "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_930_jmp_4',
        "command": 'jmp',
        "args": ['ACTION_930_start_loop_n_times_6']
    },
    {
        "identifier": 'ACTION_930_set_sprite_sequence_5',
        "command": 'set_sprite_sequence',
        "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_930_start_loop_n_times_6',
        "command": 'start_loop_n_times',
        "args": [47]
    },
    {
        "identifier": 'ACTION_930_pause_7',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_930_jmp_if_mario_in_air_8',
        "command": 'jmp_if_mario_in_air',
        "args": ['ACTION_930_ret_23']
    },
    {
        "identifier": 'ACTION_930_end_loop_9',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_930_start_loop_n_times_10',
        "command": 'start_loop_n_times',
        "args": [11]
    },
    {
        "identifier": 'ACTION_930_set_animation_speed_11',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_930_shift_z_down_pixels_12',
        "command": 'shift_z_down_pixels',
        "args": [2]
    },
    {
        "identifier": 'ACTION_930_shift_z_up_pixels_13',
        "command": 'shift_z_up_pixels',
        "args": [2]
    },
    {
        "identifier": 'ACTION_930_jmp_if_mario_in_air_14',
        "command": 'jmp_if_mario_in_air',
        "args": ['ACTION_930_ret_23']
    },
    {
        "identifier": 'ACTION_930_end_loop_15',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_930_jump_to_height_silent_16',
        "command": 'jump_to_height_silent',
        "args": [0]
    },
    {
        "identifier": 'ACTION_930_floating_on_17',
        "command": 'floating_on'
    },
    {
        "identifier": 'ACTION_930_pause_18',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_930_db_19',
        "command": 'db',
        "args": [0xfd, 0x3d, 0x07, 0x2a, 0xac]
    },
    {
        "identifier": 'ACTION_930_clear_solidity_bits_20',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS, _0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_930_visibility_off_21',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_930_object_memory_set_bit_22',
        "command": 'object_memory_set_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_930_ret_23',
        "command": 'ret'
    }
]
