from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_36_set_short_0',
        "command": 'set_short',
        "args": [0x7024, 0x0014]
    },
    {
        "identifier": 'ACTION_36_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_36_set_700C_to_pressed_button_2',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_36_dec_short_mem_3',
        "command": 'dec_short_mem',
        "args": [0x700c, 0x7024]
    },
    {
        "identifier": 'ACTION_36_mem_700C_and_const_4',
        "command": 'mem_700C_and_const',
        "args": [0x0003]
    },
    {
        "identifier": 'ACTION_36_jmp_if_700C_not_equals_short_5',
        "command": 'jmp_if_700C_not_equals_short',
        "args": [0, 'ACTION_36_load_mem_11']
    },
    {
        "identifier": 'ACTION_36_db_6',
        "command": 'db',
        "args": [0xc8, 0x07]
    },
    {
        "identifier": 'ACTION_36_add_short_7',
        "command": 'add_short',
        "args": [0x701a, 0x0080]
    },
    {
        "identifier": 'ACTION_36_add_short_8',
        "command": 'add_short',
        "args": [0x7016, 0x0040]
    },
    {
        "identifier": 'ACTION_36_db_9',
        "command": 'db',
        "args": [0x99]
    },
    {
        "identifier": 'ACTION_36_jmp_10',
        "command": 'jmp',
        "args": ['ACTION_36_visibility_on_16']
    },
    {
        "identifier": 'ACTION_36_load_mem_11',
        "command": 'load_mem',
        "args": [0x700c]
    },
    {
        "identifier": 'ACTION_36_pause_12',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_36_end_loop_13',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_36_pause_14',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_36_set_animation_speed_15',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_36_visibility_on_16',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_36_set_priority_17',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_36_shift_northwest_steps_18',
        "command": 'shift_northwest_steps',
        "args": [4]
    },
    {
        "identifier": 'ACTION_36_jmp_19',
        "command": 'jmp',
        "args": ['ACTION_32_shift_z_up_steps_20']
    },
    {
        "identifier": 'ACTION_36_ret_20',
        "command": 'ret'
    }
]
