from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_665_shadow_off_0',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_665_object_memory_set_bit_1',
        "command": 'object_memory_set_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_665_pause_2',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'ACTION_665_pause_3',
        "command": 'pause',
        "args": [90]
    },
    {
        "identifier": 'ACTION_665_pause_4',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_665_jmp_if_bit_clear_5',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 3, 'ACTION_665_visibility_on_7']
    },
    {
        "identifier": 'ACTION_665_jmp_6',
        "command": 'jmp',
        "args": ['ACTION_665_shadow_off_0']
    },
    {
        "identifier": 'ACTION_665_visibility_on_7',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_665_set_priority_8',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_665_set_sprite_sequence_9',
        "command": 'set_sprite_sequence',
        "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_665_add_z_coord_1_step_10',
        "command": 'add_z_coord_1_step'
    },
    {
        "identifier": 'ACTION_665_shift_z_up_pixels_11',
        "command": 'shift_z_up_pixels',
        "args": [12]
    },
    {
        "identifier": 'ACTION_665_set_solidity_bits_12',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_665_object_memory_clear_bit_13',
        "command": 'object_memory_clear_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_665_set_sprite_sequence_14',
        "command": 'set_sprite_sequence',
        "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_665_pause_15',
        "command": 'pause',
        "args": [48]
    },
    {
        "identifier": 'ACTION_665_set_sprite_sequence_16',
        "command": 'set_sprite_sequence',
        "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_665_dec_z_coord_1_step_17',
        "command": 'dec_z_coord_1_step'
    },
    {
        "identifier": 'ACTION_665_clear_solidity_bits_18',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_665_object_memory_set_bit_19',
        "command": 'object_memory_set_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_665_shift_z_down_pixels_20',
        "command": 'shift_z_down_pixels',
        "args": [12]
    },
    {
        "identifier": 'ACTION_665_visibility_off_21',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_665_jmp_if_random_above_66_22',
        "command": 'jmp_if_random_above_66',
        "args": [0x797c, 'ACTION_665_pause_4']
    },
    {
        "identifier": 'ACTION_665_jmp_23',
        "command": 'jmp',
        "args": ['ACTION_665_shadow_off_0']
    }
]
