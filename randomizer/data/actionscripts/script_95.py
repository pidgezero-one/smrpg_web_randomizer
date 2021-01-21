from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_95_sequence_playback_off_0',
        "command": 'sequence_playback_off'
    },
    {
        "identifier": 'ACTION_95_face_northwest_1',
        "command": 'face_northwest'
    },
    {
        "identifier": 'ACTION_95_fixed_f_coord_on_2',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_95_set_animation_speed_3',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_95_pause_4',
        "command": 'pause',
        "args": [120]
    },
    {
        "identifier": 'ACTION_95_pause_5',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'ACTION_95_start_loop_n_times_6',
        "command": 'start_loop_n_times',
        "args": [1]
    },
    {
        "identifier": 'ACTION_95_shift_east_pixels_7',
        "command": 'shift_east_pixels',
        "args": [1]
    },
    {
        "identifier": 'ACTION_95_pause_8',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_95_shift_west_pixels_9',
        "command": 'shift_west_pixels',
        "args": [1]
    },
    {
        "identifier": 'ACTION_95_pause_10',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_95_end_loop_11',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_95_pause_12',
        "command": 'pause',
        "args": [120]
    },
    {
        "identifier": 'ACTION_95_jmp_13',
        "command": 'jmp',
        "args": ['ACTION_95_sequence_playback_off_0']
    }
]
