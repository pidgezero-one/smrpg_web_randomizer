from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_345_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_345_add_short_1',
        "command": 'add_short',
        "args": [0x702c, 0x01]
    },
    {
        "identifier": 'ACTION_345_set_short_mem_2',
        "command": 'set_short_mem',
        "args": [0x700c, 0x702c]
    },
    {
        "identifier": 'ACTION_345_mem_700C_and_const_3',
        "command": 'mem_700C_and_const',
        "args": [0x0003]
    },
    {
        "identifier": 'ACTION_345_jmp_if_var_equals_short_4',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 0, 'ACTION_345_shift_f_direction_steps_6']
    },
    {
        "identifier": 'ACTION_345_set_animation_speed_5',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_345_shift_f_direction_steps_6',
        "command": 'shift_f_direction_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_345_add_short_7',
        "command": 'add_short',
        "args": [0x702c, 0x01]
    },
    {
        "identifier": 'ACTION_345_set_short_mem_8',
        "command": 'set_short_mem',
        "args": [0x700c, 0x702c]
    },
    {
        "identifier": 'ACTION_345_mem_700C_and_const_9',
        "command": 'mem_700C_and_const',
        "args": [0x0003]
    },
    {
        "identifier": 'ACTION_345_jmp_if_var_equals_short_10',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 0, 'ACTION_345_face_mario_13']
    },
    {
        "identifier": 'ACTION_345_turn_random_direction_11',
        "command": 'turn_random_direction'
    },
    {
        "identifier": 'ACTION_345_jmp_12',
        "command": 'jmp',
        "args": ['ACTION_345_set_animation_speed_0']
    },
    {
        "identifier": 'ACTION_345_face_mario_13',
        "command": 'face_mario'
    },
    {
        "identifier": 'ACTION_345_jmp_14',
        "command": 'jmp',
        "args": ['ACTION_345_set_animation_speed_0']
    }
]
