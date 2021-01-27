from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_946_set_sprite_sequence_0',
        "command": 'set_sprite_sequence',
        "args": [5, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_946_pause_1',
        "command": 'pause',
        "args": [128]
    },
    {
        "identifier": 'ACTION_946_jmp_if_random_above_128_2',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_946_start_loop_n_times_9']
    },
    {
        "identifier": 'ACTION_946_start_loop_n_times_3',
        "command": 'start_loop_n_times',
        "args": [2]
    },
    {
        "identifier": 'ACTION_946_shift_northeast_pixels_4',
        "command": 'shift_northeast_pixels',
        "args": [1]
    },
    {
        "identifier": 'ACTION_946_shift_southwest_pixels_5',
        "command": 'shift_southwest_pixels',
        "args": [1]
    },
    {
        "identifier": 'ACTION_946_end_loop_6',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_946_pause_7',
        "command": 'pause',
        "args": [128]
    },
    {
        "identifier": 'ACTION_946_jmp_8',
        "command": 'jmp',
        "args": ['ACTION_946_set_sprite_sequence_0']
    },
    {
        "identifier": 'ACTION_946_start_loop_n_times_9',
        "command": 'start_loop_n_times',
        "args": [2]
    },
    {
        "identifier": 'ACTION_946_shift_southeast_pixels_10',
        "command": 'shift_southeast_pixels',
        "args": [1]
    },
    {
        "identifier": 'ACTION_946_shift_northwest_pixels_11',
        "command": 'shift_northwest_pixels',
        "args": [1]
    },
    {
        "identifier": 'ACTION_946_end_loop_12',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_946_pause_13',
        "command": 'pause',
        "args": [128]
    },
    {
        "identifier": 'ACTION_946_jmp_14',
        "command": 'jmp',
        "args": ['ACTION_946_pause_1']
    }
]
