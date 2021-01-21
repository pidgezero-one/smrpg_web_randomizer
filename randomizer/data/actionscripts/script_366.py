from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_366_set_priority_0',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_366_set_short_1',
        "command": 'set_short',
        "args": [0x7024, 0x0014]
    },
    {
        "identifier": 'ACTION_366_set_animation_speed_2',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_366_set_700C_to_pressed_button_3',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_366_dec_short_mem_4',
        "command": 'dec_short_mem',
        "args": [0x700c, 0x7024]
    },
    {
        "identifier": 'ACTION_366_mem_700C_and_const_5',
        "command": 'mem_700C_and_const',
        "args": [0x0003]
    },
    {
        "identifier": 'ACTION_366_jmp_if_var_not_equals_short_6',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x700c, 0, 'ACTION_366_load_mem_12']
    },
    {
        "identifier": 'ACTION_366_db_7',
        "command": 'db',
        "args": [0xc8, 0x07]
    },
    {
        "identifier": 'ACTION_366_add_short_8',
        "command": 'add_short',
        "args": [0x701a, 0x0080]
    },
    {
        "identifier": 'ACTION_366_add_short_9',
        "command": 'add_short',
        "args": [0x7016, 0x0040]
    },
    {
        "identifier": 'ACTION_366_db_10',
        "command": 'db',
        "args": [0x99]
    },
    {
        "identifier": 'ACTION_366_jmp_11',
        "command": 'jmp',
        "args": ['ACTION_366_visibility_on_17']
    },
    {
        "identifier": 'ACTION_366_load_mem_12',
        "command": 'load_mem',
        "args": [0x700c]
    },
    {
        "identifier": 'ACTION_366_pause_13',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'ACTION_366_end_loop_14',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_366_pause_15',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_366_set_animation_speed_16',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_366_visibility_on_17',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_366_shift_southeast_steps_18',
        "command": 'shift_southeast_steps',
        "args": [22]
    },
    {
        "identifier": 'ACTION_366_ret_19',
        "command": 'ret'
    }
]
