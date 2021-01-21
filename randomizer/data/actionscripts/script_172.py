from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_172_fixed_f_coord_on_0',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_172_set_sprite_sequence_1',
        "command": 'set_sprite_sequence',
        "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_172_load_mem_2',
        "command": 'load_mem',
        "args": [0x702e]
    },
    {
        "identifier": 'ACTION_172_pause_3',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_172_jmp_if_mario_in_air_4',
        "command": 'jmp_if_mario_in_air',
        "args": ['ACTION_172_ret_28']
    },
    {
        "identifier": 'ACTION_172_end_loop_5',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_172_start_loop_n_times_6',
        "command": 'start_loop_n_times',
        "args": [11]
    },
    {
        "identifier": 'ACTION_172_set_animation_speed_7',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_172_shift_z_down_pixels_8',
        "command": 'shift_z_down_pixels',
        "args": [2]
    },
    {
        "identifier": 'ACTION_172_shift_z_up_pixels_9',
        "command": 'shift_z_up_pixels',
        "args": [2]
    },
    {
        "identifier": 'ACTION_172_jmp_if_mario_in_air_10',
        "command": 'jmp_if_mario_in_air',
        "args": ['ACTION_172_ret_28']
    },
    {
        "identifier": 'ACTION_172_end_loop_11',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_172_jump_to_height_silent_12',
        "command": 'jump_to_height_silent',
        "args": [0]
    },
    {
        "identifier": 'ACTION_172_floating_on_13',
        "command": 'floating_on'
    },
    {
        "identifier": 'ACTION_172_pause_14',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_172_db_15',
        "command": 'db',
        "args": [0xfd, 0x3d, 0x07, 0xa5, 0x21]
    },
    {
        "identifier": 'ACTION_172_clear_solidity_bits_16',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_172_visibility_off_17',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_172_object_memory_set_bit_18',
        "command": 'object_memory_set_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_172_shift_z_up_steps_19',
        "command": 'shift_z_up_steps',
        "args": [9]
    },
    {
        "identifier": 'ACTION_172_start_loop_n_times_20',
        "command": 'start_loop_n_times',
        "args": [4]
    },
    {
        "identifier": 'ACTION_172_pause_21',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_172_visibility_off_22',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_172_pause_23',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_172_visibility_on_24',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_172_end_loop_25',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_172_set_solidity_bits_26',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_172_object_memory_clear_bit_27',
        "command": 'object_memory_clear_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_172_ret_28',
        "command": 'ret'
    }
]
