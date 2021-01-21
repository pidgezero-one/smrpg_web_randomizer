from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_342_set_priority_0',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_342_set_700C_to_pressed_button_1',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_342_jmp_if_var_equals_short_2',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 23, 'ACTION_342_set_animation_speed_15']
    },
    {
        "identifier": 'ACTION_342_jmp_if_var_equals_short_3',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 22, 'ACTION_342_set_animation_speed_12']
    },
    {
        "identifier": 'ACTION_342_jmp_if_var_equals_short_4',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 21, 'ACTION_342_set_animation_speed_8']
    },
    {
        "identifier": 'ACTION_342_set_animation_speed_5',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_342_set_animation_speed_6',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_342_shift_southwest_steps_7',
        "command": 'shift_southwest_steps',
        "args": [7]
    },
    {
        "identifier": 'ACTION_342_set_animation_speed_8',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_342_shift_southwest_steps_9',
        "command": 'shift_southwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_342_walk_1_step_southeast_10',
        "command": 'walk_1_step_southeast'
    },
    {
        "identifier": 'ACTION_342_shift_northeast_steps_11',
        "command": 'shift_northeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_342_set_animation_speed_12',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_342_set_animation_speed_13',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_342_shift_northeast_steps_14',
        "command": 'shift_northeast_steps',
        "args": [7]
    },
    {
        "identifier": 'ACTION_342_set_animation_speed_15',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_342_shift_northeast_steps_16',
        "command": 'shift_northeast_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_342_walk_1_step_northwest_17',
        "command": 'walk_1_step_northwest'
    },
    {
        "identifier": 'ACTION_342_shift_southwest_steps_18',
        "command": 'shift_southwest_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_342_jmp_19',
        "command": 'jmp',
        "args": ['ACTION_342_set_animation_speed_5']
    }
]
