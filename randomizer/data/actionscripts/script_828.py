from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_828_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_828_set_priority_1',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_828_set_700C_to_pressed_button_2',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_828_add_3',
        "command": 'add',
        "args": [0x700c, 65517]
    },
    {
        "identifier": 'ACTION_828_load_mem_4',
        "command": 'load_mem',
        "args": [0x700c]
    },
    {
        "identifier": 'ACTION_828_pause_5',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_828_end_loop_6',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_828_set_700C_to_pressed_button_7',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_828_jmp_if_700C_equals_short_8',
        "command": 'jmp_if_700C_equals_short',
        "args": [27, 'ACTION_828_shift_northeast_steps_37']
    },
    {
        "identifier": 'ACTION_828_jmp_if_700C_equals_short_9',
        "command": 'jmp_if_700C_equals_short',
        "args": [26, 'ACTION_828_shift_southwest_steps_33']
    },
    {
        "identifier": 'ACTION_828_jmp_if_700C_equals_short_10',
        "command": 'jmp_if_700C_equals_short',
        "args": [25, 'ACTION_828_shift_northwest_steps_29']
    },
    {
        "identifier": 'ACTION_828_jmp_if_700C_equals_short_11',
        "command": 'jmp_if_700C_equals_short',
        "args": [24, 'ACTION_828_shift_southwest_steps_26']
    },
    {
        "identifier": 'ACTION_828_jmp_if_700C_equals_short_12',
        "command": 'jmp_if_700C_equals_short',
        "args": [23, 'ACTION_828_shift_southeast_steps_19']
    },
    {
        "identifier": 'ACTION_828_shift_northeast_steps_13',
        "command": 'shift_northeast_steps',
        "args": [6]
    },
    {
        "identifier": 'ACTION_828_shift_northwest_steps_14',
        "command": 'shift_northwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_828_shift_northeast_steps_15',
        "command": 'shift_northeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_828_shift_northwest_steps_16',
        "command": 'shift_northwest_steps',
        "args": [4]
    },
    {
        "identifier": 'ACTION_828_shift_northeast_steps_17',
        "command": 'shift_northeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_828_shift_northwest_steps_18',
        "command": 'shift_northwest_steps',
        "args": [5]
    },
    {
        "identifier": 'ACTION_828_shift_southeast_steps_19',
        "command": 'shift_southeast_steps',
        "args": [5]
    },
    {
        "identifier": 'ACTION_828_shift_southwest_steps_20',
        "command": 'shift_southwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_828_shift_southeast_steps_21',
        "command": 'shift_southeast_steps',
        "args": [4]
    },
    {
        "identifier": 'ACTION_828_shift_southwest_steps_22',
        "command": 'shift_southwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_828_shift_southeast_steps_23',
        "command": 'shift_southeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_828_shift_southwest_steps_24',
        "command": 'shift_southwest_steps',
        "args": [6]
    },
    {
        "identifier": 'ACTION_828_jmp_25',
        "command": 'jmp',
        "args": ['ACTION_828_shift_northeast_steps_13']
    },
    {
        "identifier": 'ACTION_828_shift_southwest_steps_26',
        "command": 'shift_southwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_828_shift_southeast_steps_27',
        "command": 'shift_southeast_steps',
        "args": [5]
    },
    {
        "identifier": 'ACTION_828_walk_1_step_southwest_28',
        "command": 'walk_1_step_southwest'
    },
    {
        "identifier": 'ACTION_828_shift_northwest_steps_29',
        "command": 'shift_northwest_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_828_shift_northeast_steps_30',
        "command": 'shift_northeast_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_828_shift_northwest_steps_31',
        "command": 'shift_northwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_828_jmp_32',
        "command": 'jmp',
        "args": ['ACTION_828_shift_southwest_steps_26']
    },
    {
        "identifier": 'ACTION_828_shift_southwest_steps_33',
        "command": 'shift_southwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_828_shift_northwest_steps_34',
        "command": 'shift_northwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_828_shift_southwest_steps_35',
        "command": 'shift_southwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_828_walk_1_step_northwest_36',
        "command": 'walk_1_step_northwest'
    },
    {
        "identifier": 'ACTION_828_shift_northeast_steps_37',
        "command": 'shift_northeast_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_828_shift_southeast_steps_38',
        "command": 'shift_southeast_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_828_walk_1_step_northeast_39',
        "command": 'walk_1_step_northeast'
    },
    {
        "identifier": 'ACTION_828_jmp_40',
        "command": 'jmp',
        "args": ['ACTION_828_shift_southwest_steps_33']
    }
]
