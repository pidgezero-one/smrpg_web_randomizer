from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_706_set_priority_0',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_706_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_706_shift_f_direction_steps_2',
        "command": 'shift_f_direction_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_706_pause_3',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'ACTION_706_turn_clockwise_45_degrees_n_times_4',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [2]
    },
    {
        "identifier": 'ACTION_706_pause_5',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'ACTION_706_turn_clockwise_45_degrees_n_times_6',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [6]
    },
    {
        "identifier": 'ACTION_706_pause_7',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_706_turn_clockwise_45_degrees_n_times_8',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [6]
    },
    {
        "identifier": 'ACTION_706_pause_9',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'ACTION_706_turn_clockwise_45_degrees_n_times_10',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [6]
    },
    {
        "identifier": 'ACTION_706_jmp_11',
        "command": 'jmp',
        "args": ['ACTION_706_shift_f_direction_steps_2']
    }
]
