from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_108_start_loop_n_times_0',
        "command": 'start_loop_n_times',
        "args": [2]
    },
    {
        "identifier": 'ACTION_108_db_1',
        "command": 'db',
        "args": [0x20, 0x04]
    },
    {
        "identifier": 'ACTION_108_db_2',
        "command": 'db',
        "args": [0x25, 0xc0, 0x06, 0x80, 0xff]
    },
    {
        "identifier": 'ACTION_108_walk_1_step_southwest_3',
        "command": 'walk_1_step_southwest'
    },
    {
        "identifier": 'ACTION_108_shift_southwest_pixels_4',
        "command": 'shift_southwest_pixels',
        "args": [11]
    },
    {
        "identifier": 'ACTION_108_bpl_26_27_28_5',
        "command": 'bpl_26_27_28'
    },
    {
        "identifier": 'ACTION_108_pause_6',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_108_end_loop_7',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_108_set_solidity_bits_8',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_108_jump_to_height_silent_9',
        "command": 'jump_to_height_silent',
        "args": [108]
    },
    {
        "identifier": 'ACTION_108_walk_1_step_southwest_10',
        "command": 'walk_1_step_southwest'
    },
    {
        "identifier": 'ACTION_108_shift_southwest_pixels_11',
        "command": 'shift_southwest_pixels',
        "args": [14]
    },
    {
        "identifier": 'ACTION_108_pause_12',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_108_db_13',
        "command": 'db',
        "args": [0x20, 0x04]
    },
    {
        "identifier": 'ACTION_108_db_14',
        "command": 'db',
        "args": [0x25, 0xc0, 0x06, 0x80, 0xff]
    },
    {
        "identifier": 'ACTION_108_walk_1_step_southwest_15',
        "command": 'walk_1_step_southwest'
    },
    {
        "identifier": 'ACTION_108_shift_southwest_pixels_16',
        "command": 'shift_southwest_pixels',
        "args": [11]
    },
    {
        "identifier": 'ACTION_108_bpl_26_27_28_17',
        "command": 'bpl_26_27_28'
    },
    {
        "identifier": 'ACTION_108_shift_southwest_pixels_18',
        "command": 'shift_southwest_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_108_clear_solidity_bits_19',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_108_clear_solidity_bits_20',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_108_visibility_off_21',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_108_ret_22',
        "command": 'ret'
    }
]
