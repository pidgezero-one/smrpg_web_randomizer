from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_284_db_0',
        "command": 'db',
        "args": [0x36]
    },
    {
        "identifier": 'ACTION_284_object_memory_set_bit_1',
        "command": 'object_memory_set_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_284_jmp_if_bit_clear_2',
        "command": 'jmp_if_bit_clear',
        "args": [0x707c, 1, 'ACTION_284_start_loop_n_times_4']
    },
    {
        "identifier": 'ACTION_284_clear_solidity_bits_3',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_284_start_loop_n_times_4',
        "command": 'start_loop_n_times',
        "args": [15]
    },
    {
        "identifier": 'ACTION_284_pause_5',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_284_visibility_off_6',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_284_pause_7',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_284_visibility_on_8',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_284_end_loop_9',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_284_set_solidity_bits_10',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_284_object_memory_clear_bit_11',
        "command": 'object_memory_clear_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_284_db_12',
        "command": 'db',
        "args": [0x37]
    },
    {
        "identifier": 'ACTION_284_ret_13',
        "command": 'ret'
    }
]
