from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_341_set_priority_0',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_341_set_700C_to_pressed_button_1',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_341_jmp_if_var_equals_short_2',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 24, 'ACTION_341_set_animation_speed_22']
    },
    {
        "identifier": 'ACTION_341_jmp_if_var_equals_short_3',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 23, 'ACTION_341_set_animation_speed_16']
    },
    {
        "identifier": 'ACTION_341_jmp_if_var_equals_short_4',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 22, 'ACTION_341_set_animation_speed_8']
    },
    {
        "identifier": 'ACTION_341_set_animation_speed_5',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_341_set_animation_speed_6',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_341_shift_southeast_steps_7',
        "command": 'shift_southeast_steps',
        "args": [5]
    },
    {
        "identifier": 'ACTION_341_set_animation_speed_8',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_341_walk_1_step_southeast_9',
        "command": 'walk_1_step_southeast'
    },
    {
        "identifier": 'ACTION_341_walk_1_step_southwest_10',
        "command": 'walk_1_step_southwest'
    },
    {
        "identifier": 'ACTION_341_set_animation_speed_11',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_341_set_animation_speed_12',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_341_shift_southwest_steps_13',
        "command": 'shift_southwest_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_341_set_animation_speed_14',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_341_walk_1_step_southeast_15',
        "command": 'walk_1_step_southeast'
    },
    {
        "identifier": 'ACTION_341_set_animation_speed_16',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_341_set_animation_speed_17',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_341_shift_northeast_steps_18',
        "command": 'shift_northeast_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_341_set_animation_speed_19',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_341_shift_northeast_steps_20',
        "command": 'shift_northeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_341_shift_northwest_steps_21',
        "command": 'shift_northwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_341_set_animation_speed_22',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_341_set_animation_speed_23',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_341_shift_northwest_steps_24',
        "command": 'shift_northwest_steps',
        "args": [5]
    },
    {
        "identifier": 'ACTION_341_set_animation_speed_25',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_341_walk_1_step_southwest_26',
        "command": 'walk_1_step_southwest'
    },
    {
        "identifier": 'ACTION_341_jmp_27',
        "command": 'jmp',
        "args": ['ACTION_341_set_animation_speed_5']
    }
]
