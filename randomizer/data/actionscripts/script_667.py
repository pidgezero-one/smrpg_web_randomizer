from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_667_shadow_off_0',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_667_object_memory_set_bit_1',
        "command": 'object_memory_set_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_667_pause_2',
        "command": 'pause',
        "args": [120]
    },
    {
        "identifier": 'ACTION_667_pause_3',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_667_jmp_if_bit_clear_4',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 5, 'ACTION_667_visibility_on_6']
    },
    {
        "identifier": 'ACTION_667_jmp_5',
        "command": 'jmp',
        "args": ['ACTION_667_shadow_off_0']
    },
    {
        "identifier": 'ACTION_667_visibility_on_6',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_667_set_priority_7',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_667_set_sprite_sequence_8',
        "command": 'set_sprite_sequence',
        "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_667_add_z_coord_1_step_9',
        "command": 'add_z_coord_1_step'
    },
    {
        "identifier": 'ACTION_667_shift_z_up_pixels_10',
        "command": 'shift_z_up_pixels',
        "args": [12]
    },
    {
        "identifier": 'ACTION_667_set_solidity_bits_11',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_667_object_memory_clear_bit_12',
        "command": 'object_memory_clear_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_667_set_sprite_sequence_13',
        "command": 'set_sprite_sequence',
        "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_667_pause_14',
        "command": 'pause',
        "args": [48]
    },
    {
        "identifier": 'ACTION_667_set_sprite_sequence_15',
        "command": 'set_sprite_sequence',
        "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_667_dec_z_coord_1_step_16',
        "command": 'dec_z_coord_1_step'
    },
    {
        "identifier": 'ACTION_667_clear_solidity_bits_17',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_667_object_memory_set_bit_18',
        "command": 'object_memory_set_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_667_shift_z_down_pixels_19',
        "command": 'shift_z_down_pixels',
        "args": [12]
    },
    {
        "identifier": 'ACTION_667_visibility_off_20',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_667_jmp_if_random_above_128_21',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_667_pause_3']
    },
    {
        "identifier": 'ACTION_667_jmp_22',
        "command": 'jmp',
        "args": ['ACTION_667_shadow_off_0']
    }
]
