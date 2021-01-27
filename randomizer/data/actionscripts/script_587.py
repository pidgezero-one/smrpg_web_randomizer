from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_587_fixed_f_coord_on_0',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_587_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_587_set_sprite_sequence_2',
        "command": 'set_sprite_sequence',
        "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_587_set_animation_speed_3',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_587_start_loop_n_times_4',
        "command": 'start_loop_n_times',
        "args": [2]
    },
    {
        "identifier": 'ACTION_587_shift_northwest_pixels_5',
        "command": 'shift_northwest_pixels',
        "args": [1]
    },
    {
        "identifier": 'ACTION_587_pause_6',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'ACTION_587_end_loop_7',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_587_start_loop_n_times_8',
        "command": 'start_loop_n_times',
        "args": [5]
    },
    {
        "identifier": 'ACTION_587_shift_southeast_pixels_9',
        "command": 'shift_southeast_pixels',
        "args": [1]
    },
    {
        "identifier": 'ACTION_587_pause_10',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'ACTION_587_end_loop_11',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_587_start_loop_n_times_12',
        "command": 'start_loop_n_times',
        "args": [2]
    },
    {
        "identifier": 'ACTION_587_shift_northwest_pixels_13',
        "command": 'shift_northwest_pixels',
        "args": [1]
    },
    {
        "identifier": 'ACTION_587_pause_14',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'ACTION_587_end_loop_15',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_587_jmp_16',
        "command": 'jmp',
        "args": ['ACTION_587_start_loop_n_times_4']
    }
]
