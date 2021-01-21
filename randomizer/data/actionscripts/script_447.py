from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_447_object_memory_set_bit_0',
        "command": 'object_memory_set_bit',
        "args": [0x3c, [6]]
    },
    {
        "identifier": 'ACTION_447_clear_solidity_bits_1',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS, _0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_447_floating_off_2',
        "command": 'floating_off'
    },
    {
        "identifier": 'ACTION_447_transfer_to_object_xy_3',
        "command": 'transfer_to_object_xy',
        "args": [AreaObjects.MARIO]
    },
    {
        "identifier": 'ACTION_447_jmp_if_bit_set_4',
        "command": 'jmp_if_bit_set',
        "args": [0x707c, 2, 'ACTION_447_visibility_off_17']
    },
    {
        "identifier": 'ACTION_447_jmp_if_bit_set_5',
        "command": 'jmp_if_bit_set',
        "args": [0x707c, 3, 'ACTION_447_visibility_off_17']
    },
    {
        "identifier": 'ACTION_447_jmp_if_random_above_128_6',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_447_shift_xy_pixels_9']
    },
    {
        "identifier": 'ACTION_447_shift_xy_pixels_7',
        "command": 'shift_xy_pixels',
        "args": [4, 4]
    },
    {
        "identifier": 'ACTION_447_jmp_8',
        "command": 'jmp',
        "args": ['ACTION_447_sequence_looping_on_10']
    },
    {
        "identifier": 'ACTION_447_shift_xy_pixels_9',
        "command": 'shift_xy_pixels',
        "args": [252, 252]
    },
    {
        "identifier": 'ACTION_447_sequence_looping_on_10',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_447_set_sprite_sequence_11',
        "command": 'set_sprite_sequence',
        "args": [1, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_447_start_loop_n_times_12',
        "command": 'start_loop_n_times',
        "args": [23]
    },
    {
        "identifier": 'ACTION_447_jmp_if_bit_set_13',
        "command": 'jmp_if_bit_set',
        "args": [0x707c, 2, 'ACTION_447_visibility_off_17']
    },
    {
        "identifier": 'ACTION_447_jmp_if_bit_set_14',
        "command": 'jmp_if_bit_set',
        "args": [0x707c, 3, 'ACTION_447_visibility_off_17']
    },
    {
        "identifier": 'ACTION_447_pause_15',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_447_end_loop_16',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_447_visibility_off_17',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_447_ret_18',
        "command": 'ret'
    }
]
