from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_606_set_priority_0',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_606_shift_f_direction_steps_1',
        "command": 'shift_f_direction_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_606_set_animation_speed_2',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_606_shift_z_down_pixels_3',
        "command": 'shift_z_down_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_606_add_z_coord_1_step_4',
        "command": 'add_z_coord_1_step'
    },
    {
        "identifier": 'ACTION_606_dec_z_coord_1_step_5',
        "command": 'dec_z_coord_1_step'
    },
    {
        "identifier": 'ACTION_606_shift_z_up_pixels_6',
        "command": 'shift_z_up_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_606_set_animation_speed_7',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_606_turn_clockwise_45_degrees_n_times_8',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [4]
    },
    {
        "identifier": 'ACTION_606_shift_f_direction_steps_9',
        "command": 'shift_f_direction_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_606_turn_clockwise_45_degrees_n_times_10',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [4]
    },
    {
        "identifier": 'ACTION_606_jmp_11',
        "command": 'jmp',
        "args": ['ACTION_606_set_priority_0']
    }
]
