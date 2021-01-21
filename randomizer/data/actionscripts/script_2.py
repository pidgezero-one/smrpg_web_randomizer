from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_2_object_memory_set_bit_0',
        "command": 'object_memory_set_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_2_jmp_if_bit_clear_1',
        "command": 'jmp_if_bit_clear',
        "args": [0x707c, 1, 'ACTION_2_start_loop_n_times_3']
    },
    {
        "identifier": 'ACTION_2_clear_solidity_bits_2',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_2_start_loop_n_times_3',
        "command": 'start_loop_n_times',
        "args": [15]
    },
    {
        "identifier": 'ACTION_2_pause_4',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_2_visibility_off_5',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_2_pause_6',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_2_visibility_on_7',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_2_end_loop_8',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_2_set_solidity_bits_9',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_2_object_memory_clear_bit_10',
        "command": 'object_memory_clear_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_2_ret_11',
        "command": 'ret'
    }
]
