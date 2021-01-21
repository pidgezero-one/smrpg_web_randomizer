from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_469_set_solidity_bits_0',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_469_sequence_looping_on_1',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_469_set_animation_speed_2',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_469_start_loop_n_times_3',
        "command": 'start_loop_n_times',
        "args": [119]
    },
    {
        "identifier": 'ACTION_469_pause_4',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_469_db_5',
        "command": 'db',
        "args": [0x3b, 0x00, 0x00, 0x03, 0x8e, 0x5a]
    },
    {
        "identifier": 'ACTION_469_jmp_6',
        "command": 'jmp',
        "args": ['ACTION_469_end_loop_8']
    },
    {
        "identifier": 'ACTION_469_db_7',
        "command": 'db',
        "args": [0x3c, 0x00, 0x20, 0x99, 0x5a]
    },
    {
        "identifier": 'ACTION_469_end_loop_8',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_469_turn_clockwise_45_degrees_n_times_9',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [4]
    },
    {
        "identifier": 'ACTION_469_jmp_10',
        "command": 'jmp',
        "args": ['ACTION_469_start_loop_n_times_3']
    },
    {
        "identifier": 'ACTION_469_set_bit_11',
        "command": 'set_bit',
        "args": [0x7044, 4]
    },
    {
        "identifier": 'ACTION_469_ret_12',
        "command": 'ret'
    }
]
