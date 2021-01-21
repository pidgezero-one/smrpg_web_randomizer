from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_50_object_memory_set_bit_0',
        "command": 'object_memory_set_bit',
        "args": [0x0b, [3]]
    },
    {
        "identifier": 'ACTION_50_clear_solidity_bits_1',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_50_set_700C_to_pressed_button_2',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_50_jmp_if_var_equals_short_3',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 21, 'ACTION_50_pause_26']
    },
    {
        "identifier": 'ACTION_50_pause_4',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'ACTION_50_walk_1_step_northwest_5',
        "command": 'walk_1_step_northwest'
    },
    {
        "identifier": 'ACTION_50_pause_6',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_50_walk_1_step_southwest_7',
        "command": 'walk_1_step_southwest'
    },
    {
        "identifier": 'ACTION_50_pause_8',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_50_shift_southeast_steps_9',
        "command": 'shift_southeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_50_pause_10',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_50_walk_1_step_northeast_11',
        "command": 'walk_1_step_northeast'
    },
    {
        "identifier": 'ACTION_50_pause_12',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_50_add_short_13',
        "command": 'add_short',
        "args": [0x702c, 0x01]
    },
    {
        "identifier": 'ACTION_50_walk_1_step_northwest_14',
        "command": 'walk_1_step_northwest'
    },
    {
        "identifier": 'ACTION_50_pause_15',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_50_shift_southwest_steps_16',
        "command": 'shift_southwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_50_pause_17',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_50_walk_1_step_northwest_18',
        "command": 'walk_1_step_northwest'
    },
    {
        "identifier": 'ACTION_50_pause_19',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_50_shift_northeast_steps_20',
        "command": 'shift_northeast_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_50_pause_21',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_50_walk_1_step_southeast_22',
        "command": 'walk_1_step_southeast'
    },
    {
        "identifier": 'ACTION_50_pause_23',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_50_walk_1_step_southwest_24',
        "command": 'walk_1_step_southwest'
    },
    {
        "identifier": 'ACTION_50_jmp_25',
        "command": 'jmp',
        "args": ['ACTION_50_pause_4']
    },
    {
        "identifier": 'ACTION_50_pause_26',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'ACTION_50_walk_1_step_northwest_27',
        "command": 'walk_1_step_northwest'
    },
    {
        "identifier": 'ACTION_50_pause_28',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_50_shift_northeast_steps_29',
        "command": 'shift_northeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_50_pause_30',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_50_walk_1_step_southeast_31',
        "command": 'walk_1_step_southeast'
    },
    {
        "identifier": 'ACTION_50_shift_southwest_steps_32',
        "command": 'shift_southwest_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_50_walk_1_step_southeast_33',
        "command": 'walk_1_step_southeast'
    },
    {
        "identifier": 'ACTION_50_walk_1_step_northeast_34',
        "command": 'walk_1_step_northeast'
    },
    {
        "identifier": 'ACTION_50_walk_1_step_northwest_35',
        "command": 'walk_1_step_northwest'
    },
    {
        "identifier": 'ACTION_50_jmp_if_random_above_128_36',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_50_pause_26']
    },
    {
        "identifier": 'ACTION_50_shift_northeast_steps_37',
        "command": 'shift_northeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_50_walk_1_step_southeast_38',
        "command": 'walk_1_step_southeast'
    },
    {
        "identifier": 'ACTION_50_pause_39',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'ACTION_50_shift_northwest_steps_40',
        "command": 'shift_northwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_50_shift_southwest_steps_41',
        "command": 'shift_southwest_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_50_walk_1_step_southeast_42',
        "command": 'walk_1_step_southeast'
    },
    {
        "identifier": 'ACTION_50_walk_1_step_northeast_43',
        "command": 'walk_1_step_northeast'
    },
    {
        "identifier": 'ACTION_50_jmp_44',
        "command": 'jmp',
        "args": ['ACTION_50_pause_26']
    }
]
