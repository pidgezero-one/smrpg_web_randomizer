from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_344_set_700C_to_object_coord_0',
        "command": 'set_700C_to_object_coord',
        "args": [AreaObjects.DUMMY_0X07, Coords.F, []]
    },
    {
        "identifier": 'ACTION_344_mem_700C_and_const_1',
        "command": 'mem_700C_and_const',
        "args": [0x0007]
    },
    {
        "identifier": 'ACTION_344_jmp_if_700C_not_equals_short_2',
        "command": 'jmp_if_700C_not_equals_short',
        "args": [3, 'ACTION_344_sequence_looping_on_4']
    },
    {
        "identifier": 'ACTION_344_shift_xy_pixels_3',
        "command": 'shift_xy_pixels',
        "args": [9, 8]
    },
    {
        "identifier": 'ACTION_344_sequence_looping_on_4',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_344_fixed_f_coord_on_5',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_344_set_700C_to_pressed_button_6',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_344_mem_700C_and_const_7',
        "command": 'mem_700C_and_const',
        "args": [0x0007]
    },
    {
        "identifier": 'ACTION_344_jmp_if_700C_equals_short_8',
        "command": 'jmp_if_700C_equals_short',
        "args": [7, 'ACTION_344_pause_22']
    },
    {
        "identifier": 'ACTION_344_jmp_if_700C_equals_short_9',
        "command": 'jmp_if_700C_equals_short',
        "args": [6, 'ACTION_344_pause_21']
    },
    {
        "identifier": 'ACTION_344_jmp_if_700C_equals_short_10',
        "command": 'jmp_if_700C_equals_short',
        "args": [5, 'ACTION_344_pause_20']
    },
    {
        "identifier": 'ACTION_344_jmp_if_700C_equals_short_11',
        "command": 'jmp_if_700C_equals_short',
        "args": [4, 'ACTION_344_pause_19']
    },
    {
        "identifier": 'ACTION_344_jmp_if_700C_equals_short_12',
        "command": 'jmp_if_700C_equals_short',
        "args": [3, 'ACTION_344_pause_18']
    },
    {
        "identifier": 'ACTION_344_jmp_if_700C_equals_short_13',
        "command": 'jmp_if_700C_equals_short',
        "args": [2, 'ACTION_344_pause_17']
    },
    {
        "identifier": 'ACTION_344_jmp_if_700C_equals_short_14',
        "command": 'jmp_if_700C_equals_short',
        "args": [1, 'ACTION_344_pause_16']
    },
    {
        "identifier": 'ACTION_344_pause_15',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_344_pause_16',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_344_pause_17',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_344_pause_18',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_344_pause_19',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_344_pause_20',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_344_pause_21',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_344_pause_22',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_344_jmp_23',
        "command": 'jmp',
        "args": ['ACTION_344_pause_22']
    }
]
