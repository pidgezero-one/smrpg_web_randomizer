from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_86_sequence_playback_off_0',
        "command": 'sequence_playback_off'
    },
    {
        "identifier": 'ACTION_86_face_northwest_1',
        "command": 'face_northwest'
    },
    {
        "identifier": 'ACTION_86_fixed_f_coord_on_2',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_86_set_animation_speed_3',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_86_pause_4',
        "command": 'pause',
        "args": [120]
    },
    {
        "identifier": 'ACTION_86_start_loop_n_times_5',
        "command": 'start_loop_n_times',
        "args": [1]
    },
    {
        "identifier": 'ACTION_86_shift_east_pixels_6',
        "command": 'shift_east_pixels',
        "args": [1]
    },
    {
        "identifier": 'ACTION_86_pause_7',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_86_shift_west_pixels_8',
        "command": 'shift_west_pixels',
        "args": [1]
    },
    {
        "identifier": 'ACTION_86_pause_9',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_86_end_loop_10',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_86_jmp_11',
        "command": 'jmp',
        "args": ['ACTION_86_sequence_playback_off_0']
    }
]
