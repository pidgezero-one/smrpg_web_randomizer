from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_471_set_vram_priority_0',
        "command": 'set_vram_priority',
        "args": [VramPriority.NORMAL]
    },
    {
        "identifier": 'ACTION_471_set_priority_1',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_471_clear_solidity_bits_2',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_471_set_solidity_bits_3',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_471_object_memory_clear_bit_4',
        "command": 'object_memory_clear_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_471_fixed_f_coord_off_5',
        "command": 'fixed_f_coord_off'
    },
    {
        "identifier": 'ACTION_471_set_solidity_bits_6',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_471_object_memory_set_bit_7',
        "command": 'object_memory_set_bit',
        "args": [0x09, [7]]
    },
    {
        "identifier": 'ACTION_471_db_8',
        "command": 'db',
        "args": [0xfd, 0x12]
    },
    {
        "identifier": 'ACTION_471_set_animation_speed_9',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_471_set_700C_to_pressed_button_10',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_471_mem_700C_and_const_11',
        "command": 'mem_700C_and_const',
        "args": [0x0003]
    },
    {
        "identifier": 'ACTION_471_jmp_if_var_equals_short_12',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 0, 'ACTION_471_transfer_to_xyzf_18']
    },
    {
        "identifier": 'ACTION_471_jmp_if_var_equals_short_13',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 1, 'ACTION_471_transfer_to_xyzf_21']
    },
    {
        "identifier": 'ACTION_471_jmp_if_var_equals_short_14',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 2, 'ACTION_471_transfer_to_xyzf_24']
    },
    {
        "identifier": 'ACTION_471_transfer_to_xyzf_15',
        "command": 'transfer_to_xyzf',
        "args": [18, 46, 0, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_471_face_northwest_16',
        "command": 'face_northwest'
    },
    {
        "identifier": 'ACTION_471_jmp_17',
        "command": 'jmp',
        "args": ['ACTION_471_visibility_on_26']
    },
    {
        "identifier": 'ACTION_471_transfer_to_xyzf_18',
        "command": 'transfer_to_xyzf',
        "args": [17, 47, 0, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_471_face_northwest_19',
        "command": 'face_northwest'
    },
    {
        "identifier": 'ACTION_471_jmp_20',
        "command": 'jmp',
        "args": ['ACTION_471_visibility_on_26']
    },
    {
        "identifier": 'ACTION_471_transfer_to_xyzf_21',
        "command": 'transfer_to_xyzf',
        "args": [3, 36, 0, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_471_face_northeast_22',
        "command": 'face_northeast'
    },
    {
        "identifier": 'ACTION_471_jmp_23',
        "command": 'jmp',
        "args": ['ACTION_471_visibility_on_26']
    },
    {
        "identifier": 'ACTION_471_transfer_to_xyzf_24',
        "command": 'transfer_to_xyzf',
        "args": [3, 37, 0, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_471_face_northeast_25',
        "command": 'face_northeast'
    },
    {
        "identifier": 'ACTION_471_visibility_on_26',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_471_shift_f_direction_steps_27',
        "command": 'shift_f_direction_steps',
        "args": [15]
    },
    {
        "identifier": 'ACTION_471_jmp_28',
        "command": 'jmp',
        "args": ['ACTION_714_turn_clockwise_45_degrees_12']
    }
]
