from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_907_clear_solidity_bits_0',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_907_set_solidity_bits_1',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS, _0x0AFlags.CANT_JUMP_THROUGH]]
    },
    {
        "identifier": 'ACTION_907_set_vram_priority_2',
        "command": 'set_vram_priority',
        "args": [VramPriority.PRIORITY_3]
    },
    {
        "identifier": 'ACTION_907_set_sprite_sequence_3',
        "command": 'set_sprite_sequence',
        "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_907_jump_to_height_silent_4',
        "command": 'jump_to_height_silent',
        "args": [48]
    },
    {
        "identifier": 'ACTION_907_floating_on_5',
        "command": 'floating_on'
    },
    {
        "identifier": 'ACTION_907_face_southeast_6',
        "command": 'face_southeast'
    },
    {
        "identifier": 'ACTION_907_jmp_if_bit_set_7',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 7, 'ACTION_907_set_object_memory_bits_9']
    },
    {
        "identifier": 'ACTION_907_face_southwest_8',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_907_set_object_memory_bits_9',
        "command": 'set_object_memory_bits',
        "args": [0x0b, bits=[0]]
    },
    {
        "identifier": 'ACTION_907_walk_1_step_f_direction_10',
        "command": 'walk_1_step_f_direction'
    },
    {
        "identifier": 'ACTION_907_set_solidity_bits_11',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_907_walk_1_step_f_direction_12',
        "command": 'walk_1_step_f_direction'
    },
    {
        "identifier": 'ACTION_907_set_vram_priority_13',
        "command": 'set_vram_priority',
        "args": [VramPriority.NORMAL]
    },
    {
        "identifier": 'ACTION_907_shift_f_direction_steps_14',
        "command": 'shift_f_direction_steps',
        "args": [6]
    },
    {
        "identifier": 'ACTION_907_start_loop_n_times_15',
        "command": 'start_loop_n_times',
        "args": [7]
    },
    {
        "identifier": 'ACTION_907_visibility_on_16',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_907_pause_17',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_907_visibility_off_18',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_907_pause_19',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_907_end_loop_20',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_907_object_memory_set_bit_21',
        "command": 'object_memory_set_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_907_visibility_off_22',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_907_ret_23',
        "command": 'ret'
    }
]
