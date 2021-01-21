from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_209_fixed_f_coord_on_0',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_209_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_209_pause_2',
        "command": 'pause',
        "args": [90]
    },
    {
        "identifier": 'ACTION_209_start_loop_n_times_3',
        "command": 'start_loop_n_times',
        "args": [1]
    },
    {
        "identifier": 'ACTION_209_shift_southwest_pixels_4',
        "command": 'shift_southwest_pixels',
        "args": [2]
    },
    {
        "identifier": 'ACTION_209_shift_northeast_pixels_5',
        "command": 'shift_northeast_pixels',
        "args": [2]
    },
    {
        "identifier": 'ACTION_209_pause_6',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_209_end_loop_7',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_209_jmp_8',
        "command": 'jmp',
        "args": ['ACTION_209_pause_2']
    }
]
