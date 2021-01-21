from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_933_clear_solidity_bits_0',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_933_object_memory_set_bit_1',
        "command": 'object_memory_set_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_933_visibility_off_2',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_933_floating_off_3',
        "command": 'floating_off'
    },
    {
        "identifier": 'ACTION_933_transfer_to_object_xy_4',
        "command": 'transfer_to_object_xy',
        "args": [AreaObjects.NPC_0]
    },
    {
        "identifier": 'ACTION_933_transfer_xyzf_pixels_5',
        "command": 'transfer_xyzf_pixels',
        "args": [254, 4, 18, RadialDirections.SOUTHEAST]
    },
    {
        "identifier": 'ACTION_933_pause_6',
        "command": 'pause',
        "args": [52]
    },
    {
        "identifier": 'ACTION_933_visibility_on_7',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_933_object_memory_clear_bit_8',
        "command": 'object_memory_clear_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_933_floating_on_9',
        "command": 'floating_on'
    },
    {
        "identifier": 'ACTION_933_set_solidity_bits_10',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_933_set_random_11',
        "command": 'set_random',
        "args": [0x700c, 8]
    },
    {
        "identifier": 'ACTION_933_face_east_12',
        "command": 'face_east'
    },
    {
        "identifier": 'ACTION_933_jmp_if_random_above_128_13',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_933_jump_to_height_silent_23']
    },
    {
        "identifier": 'ACTION_933_jmp_if_random_above_128_14',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_933_jump_to_height_silent_19']
    },
    {
        "identifier": 'ACTION_933_jump_to_height_silent_15',
        "command": 'jump_to_height_silent',
        "args": [128]
    },
    {
        "identifier": 'ACTION_933_shift_f_direction_steps_16',
        "command": 'shift_f_direction_steps',
        "args": [4]
    },
    {
        "identifier": 'ACTION_933_set_solidity_bits_17',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_933_jmp_18',
        "command": 'jmp',
        "args": ['ACTION_727_jmp_if_var_equals_byte_0']
    },
    {
        "identifier": 'ACTION_933_jump_to_height_silent_19',
        "command": 'jump_to_height_silent',
        "args": [80]
    },
    {
        "identifier": 'ACTION_933_shift_f_direction_steps_20',
        "command": 'shift_f_direction_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_933_set_solidity_bits_21',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_933_jmp_22',
        "command": 'jmp',
        "args": ['ACTION_727_jmp_if_var_equals_byte_0']
    },
    {
        "identifier": 'ACTION_933_jump_to_height_silent_23',
        "command": 'jump_to_height_silent',
        "args": [160]
    },
    {
        "identifier": 'ACTION_933_shift_f_direction_steps_24',
        "command": 'shift_f_direction_steps',
        "args": [6]
    },
    {
        "identifier": 'ACTION_933_set_solidity_bits_25',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_933_jmp_26',
        "command": 'jmp',
        "args": ['ACTION_727_jmp_if_var_equals_byte_0']
    }
]
