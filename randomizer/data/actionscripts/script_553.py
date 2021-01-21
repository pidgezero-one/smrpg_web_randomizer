from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_553_shift_east_pixels_0',
        "command": 'shift_east_pixels',
        "args": [21]
    },
    {
        "identifier": 'ACTION_553_shift_south_pixels_1',
        "command": 'shift_south_pixels',
        "args": [5]
    },
    {
        "identifier": 'ACTION_553_shift_southwest_pixels_2',
        "command": 'shift_southwest_pixels',
        "args": [1]
    },
    {
        "identifier": 'ACTION_553_set_700C_to_pressed_button_3',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_553_jmp_if_var_equals_short_4',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 30, 'ACTION_553_set_priority_15']
    },
    {
        "identifier": 'ACTION_553_set_sprite_sequence_5',
        "command": 'set_sprite_sequence',
        "args": [4, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_553_jmp_if_var_equals_short_6',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 20, 'ACTION_553_set_priority_12']
    },
    {
        "identifier": 'ACTION_553_jmp_if_var_equals_short_7',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 22, 'ACTION_553_set_priority_12']
    },
    {
        "identifier": 'ACTION_553_jmp_if_var_equals_short_8',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 24, 'ACTION_553_set_priority_12']
    },
    {
        "identifier": 'ACTION_553_set_priority_9',
        "command": 'set_priority',
        "args": [2]
    },
    {
        "identifier": 'ACTION_553_visibility_off_10',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_553_ret_11',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_553_set_priority_12',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_553_visibility_off_13',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_553_ret_14',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_553_set_priority_15',
        "command": 'set_priority',
        "args": [2]
    },
    {
        "identifier": 'ACTION_553_set_sprite_sequence_16',
        "command": 'set_sprite_sequence',
        "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_553_visibility_off_17',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_553_ret_18',
        "command": 'ret'
    }
]
