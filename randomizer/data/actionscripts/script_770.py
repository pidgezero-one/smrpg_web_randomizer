from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_770_set_vram_priority_0',
        "command": 'set_vram_priority',
        "args": [VramPriority.NORMAL]
    },
    {
        "identifier": 'ACTION_770_set_priority_1',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_770_set_solidity_bits_2',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_770_object_memory_clear_bit_3',
        "command": 'object_memory_clear_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_770_fixed_f_coord_off_4',
        "command": 'fixed_f_coord_off'
    },
    {
        "identifier": 'ACTION_770_object_memory_set_bit_5',
        "command": 'object_memory_set_bit',
        "args": [0x08, [4]]
    },
    {
        "identifier": 'ACTION_770_floating_on_6',
        "command": 'floating_on'
    },
    {
        "identifier": 'ACTION_770_set_animation_speed_7',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_770_set_700C_to_pressed_button_8',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_770_mem_700C_and_const_9',
        "command": 'mem_700C_and_const',
        "args": [0x0001]
    },
    {
        "identifier": 'ACTION_770_jmp_if_var_equals_short_10',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 0, 'ACTION_770_transfer_to_xyzf_14']
    },
    {
        "identifier": 'ACTION_770_transfer_to_xyzf_11',
        "command": 'transfer_to_xyzf',
        "args": [15, 37, 0, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_770_face_northwest_12',
        "command": 'face_northwest'
    },
    {
        "identifier": 'ACTION_770_jmp_13',
        "command": 'jmp',
        "args": ['ACTION_770_visibility_on_16']
    },
    {
        "identifier": 'ACTION_770_transfer_to_xyzf_14',
        "command": 'transfer_to_xyzf',
        "args": [2, 37, 0, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_770_face_northeast_15',
        "command": 'face_northeast'
    },
    {
        "identifier": 'ACTION_770_visibility_on_16',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_770_shift_f_direction_steps_17',
        "command": 'shift_f_direction_steps',
        "args": [10]
    },
    {
        "identifier": 'ACTION_770_jmp_18',
        "command": 'jmp',
        "args": ['ACTION_769_face_mario_6']
    }
]
