from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_721_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_721_sequence_looping_on_1',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_721_shift_f_direction_steps_2',
        "command": 'shift_f_direction_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_721_set_700C_to_object_coord_3',
        "command": 'set_700C_to_object_coord',
        "args": [AreaObjects.DUMMY_0X07, Coords.F, []]
    },
    {
        "identifier": 'ACTION_721_set_70A0_short_mem_to_700C_4',
        "command": 'set_70A0_short_mem_to_700C',
        "args": [0x70ae]
    },
    {
        "identifier": 'ACTION_721_start_loop_n_times_5',
        "command": 'start_loop_n_times',
        "args": [5]
    },
    {
        "identifier": 'ACTION_721_jump_to_height_6',
        "command": 'jump_to_height',
        "args": [56]
    },
    {
        "identifier": 'ACTION_721_pause_7',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_721_db_8',
        "command": 'db',
        "args": [0xfd, 0x3d, 0x07, 0x92, 0x85]
    },
    {
        "identifier": 'ACTION_721_turn_random_direction_9',
        "command": 'turn_random_direction'
    },
    {
        "identifier": 'ACTION_721_end_loop_10',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_721_set_700C_to_70A0_short_mem_11',
        "command": 'set_700C_to_70A0_short_mem',
        "args": [0x70ae]
    },
    {
        "identifier": 'ACTION_721_face_east_7C_12',
        "command": 'face_east_7C'
    },
    {
        "identifier": 'ACTION_721_turn_clockwise_45_degrees_n_times_13',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [4]
    },
    {
        "identifier": 'ACTION_721_jmp_14',
        "command": 'jmp',
        "args": ['ACTION_721_set_animation_speed_0']
    }
]
