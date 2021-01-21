from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_659_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_659_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_659_start_loop_n_times_2',
        "command": 'start_loop_n_times',
        "args": [3]
    },
    {
        "identifier": 'ACTION_659_shift_northeast_steps_3',
        "command": 'shift_northeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_659_db_4',
        "command": 'db',
        "args": [0x3a, 0x00, 0x00, 0x04, 0x81, 0x78]
    },
    {
        "identifier": 'ACTION_659_end_loop_5',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_659_start_loop_n_times_6',
        "command": 'start_loop_n_times',
        "args": [3]
    },
    {
        "identifier": 'ACTION_659_shift_southwest_steps_7',
        "command": 'shift_southwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_659_db_8',
        "command": 'db',
        "args": [0x3a, 0x00, 0x00, 0x04, 0x81, 0x78]
    },
    {
        "identifier": 'ACTION_659_end_loop_9',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_659_jmp_10',
        "command": 'jmp',
        "args": ['ACTION_659_set_animation_speed_0']
    },
    {
        "identifier": 'ACTION_659_set_animation_speed_11',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_659_set_animation_speed_12',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_659_face_mario_13',
        "command": 'face_mario'
    },
    {
        "identifier": 'ACTION_659_shift_f_direction_steps_14',
        "command": 'shift_f_direction_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_659_jmp_15',
        "command": 'jmp',
        "args": ['ACTION_659_set_animation_speed_0']
    }
]
