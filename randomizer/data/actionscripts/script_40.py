from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_40_start_loop_n_times_0',
        "command": 'start_loop_n_times',
        "args": [2]
    },
    {
        "identifier": 'ACTION_40_pause_1',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_40_jmp_if_bit_clear_2',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 1, 'ACTION_40_pause_1']
    },
    {
        "identifier": 'ACTION_40_set_short_3',
        "command": 'set_short',
        "args": [0x7016, 0x3b00]
    },
    {
        "identifier": 'ACTION_40_set_short_4',
        "command": 'set_short',
        "args": [0x7018, 0x0e80]
    },
    {
        "identifier": 'ACTION_40_set_short_5',
        "command": 'set_short',
        "args": [0x701a, 0x0000]
    },
    {
        "identifier": 'ACTION_40_db_6',
        "command": 'db',
        "args": [0x99]
    },
    {
        "identifier": 'ACTION_40_visibility_on_7',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_40_sequence_looping_on_8',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_40_set_sprite_sequence_9',
        "command": 'set_sprite_sequence',
        "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_40_pause_10',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'ACTION_40_visibility_off_11',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_40_end_loop_12',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_40_ret_13',
        "command": 'ret'
    }
]
