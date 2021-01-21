from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_649_face_southwest_0',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_649_fixed_f_coord_on_1',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_649_set_animation_speed_2',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_649_walk_1_step_southwest_3',
        "command": 'walk_1_step_southwest'
    },
    {
        "identifier": 'ACTION_649_sequence_looping_on_4',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_649_db_5',
        "command": 'db',
        "args": [0x3b, 0x00, 0x00, 0x08, 0xae, 0x76]
    },
    {
        "identifier": 'ACTION_649_pause_6',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_649_jmp_7',
        "command": 'jmp',
        "args": ['ACTION_649_set_animation_speed_14']
    },
    {
        "identifier": 'ACTION_649_start_loop_n_times_8',
        "command": 'start_loop_n_times',
        "args": [4]
    },
    {
        "identifier": 'ACTION_649_play_sound_9',
        "command": 'play_sound',
        "args": [Sounds._058_INSERT, 4]
    },
    {
        "identifier": 'ACTION_649_pause_10',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_649_play_sound_11',
        "command": 'play_sound',
        "args": [Sounds._058_INSERT, 4]
    },
    {
        "identifier": 'ACTION_649_pause_12',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'ACTION_649_end_loop_13',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_649_set_animation_speed_14',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_649_walk_1_step_northeast_15',
        "command": 'walk_1_step_northeast'
    },
    {
        "identifier": 'ACTION_649_sequence_looping_off_16',
        "command": 'sequence_looping_off'
    },
    {
        "identifier": 'ACTION_649_pause_17',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'ACTION_649_jmp_18',
        "command": 'jmp',
        "args": ['ACTION_649_set_animation_speed_2']
    }
]
