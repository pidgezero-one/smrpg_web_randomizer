from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_554_shift_southwest_pixels_0',
        "command": 'shift_southwest_pixels',
        "args": [7]
    },
    {
        "identifier": 'ACTION_554_shift_southeast_pixels_1',
        "command": 'shift_southeast_pixels',
        "args": [3]
    },
    {
        "identifier": 'ACTION_554_shift_north_pixels_2',
        "command": 'shift_north_pixels',
        "args": [7]
    },
    {
        "identifier": 'ACTION_554_set_sprite_sequence_3',
        "command": 'set_sprite_sequence',
        "args": [5, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_554_set_700C_to_pressed_button_4',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_554_jmp_if_700C_equals_short_5',
        "command": 'jmp_if_700C_equals_short',
        "args": [31, 'ACTION_554_set_priority_16']
    },
    {
        "identifier": 'ACTION_554_set_sprite_sequence_6',
        "command": 'set_sprite_sequence',
        "args": [5, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_554_jmp_if_700C_equals_short_7',
        "command": 'jmp_if_700C_equals_short',
        "args": [21, 'ACTION_554_set_priority_13']
    },
    {
        "identifier": 'ACTION_554_jmp_if_700C_equals_short_8',
        "command": 'jmp_if_700C_equals_short',
        "args": [22, 'ACTION_554_set_priority_13']
    },
    {
        "identifier": 'ACTION_554_jmp_if_700C_equals_short_9',
        "command": 'jmp_if_700C_equals_short',
        "args": [25, 'ACTION_554_set_priority_13']
    },
    {
        "identifier": 'ACTION_554_set_priority_10',
        "command": 'set_priority',
        "args": [2]
    },
    {
        "identifier": 'ACTION_554_visibility_off_11',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_554_ret_12',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_554_set_priority_13',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_554_visibility_off_14',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_554_ret_15',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_554_set_priority_16',
        "command": 'set_priority',
        "args": [2]
    },
    {
        "identifier": 'ACTION_554_set_sprite_sequence_17',
        "command": 'set_sprite_sequence',
        "args": [1, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_554_visibility_off_18',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_554_ret_19',
        "command": 'ret'
    }
]
