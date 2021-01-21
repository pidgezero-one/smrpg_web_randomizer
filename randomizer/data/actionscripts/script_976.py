from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_976_set_short_0',
        "command": 'set_short',
        "args": [0x7034, 0x0001]
    },
    {
        "identifier": 'ACTION_976_db_1',
        "command": 'db',
        "args": [0xc7, 0x07]
    },
    {
        "identifier": 'ACTION_976_start_loop_n_times_2',
        "command": 'start_loop_n_times',
        "args": [2]
    },
    {
        "identifier": 'ACTION_976_add_short_3',
        "command": 'add_short',
        "args": [0x7034, 0x0001]
    },
    {
        "identifier": 'ACTION_976_add_short_4',
        "command": 'add_short',
        "args": [0x7014, 0x0008]
    },
    {
        "identifier": 'ACTION_976_create_packet_at_7010_coords_jmp_if_null_5',
        "command": 'create_packet_at_7010_coords_jmp_if_null',
        "args": [NPCPackets._032_BLUE_CLOUD, 'ACTION_976_end_loop_7']
    },
    {
        "identifier": 'ACTION_976_pause_6',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_976_end_loop_7',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_976_set_short_8',
        "command": 'set_short',
        "args": [0x7034, 0x0001]
    },
    {
        "identifier": 'ACTION_976_db_9',
        "command": 'db',
        "args": [0xc7, 0x07]
    },
    {
        "identifier": 'ACTION_976_start_loop_n_times_10',
        "command": 'start_loop_n_times',
        "args": [2]
    },
    {
        "identifier": 'ACTION_976_add_short_11',
        "command": 'add_short',
        "args": [0x7034, 0x0001]
    },
    {
        "identifier": 'ACTION_976_add_short_12',
        "command": 'add_short',
        "args": [0x7014, 0x0008]
    },
    {
        "identifier": 'ACTION_976_create_packet_at_7010_coords_jmp_if_null_13',
        "command": 'create_packet_at_7010_coords_jmp_if_null',
        "args": [NPCPackets._032_BLUE_CLOUD, 'ACTION_976_end_loop_15']
    },
    {
        "identifier": 'ACTION_976_pause_14',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_976_end_loop_15',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_976_ret_16',
        "command": 'ret'
    }
]
