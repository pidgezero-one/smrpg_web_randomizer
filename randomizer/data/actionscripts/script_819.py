from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_819_set_priority_0',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_819_sequence_looping_off_1',
        "command": 'sequence_looping_off'
    },
    {
        "identifier": 'ACTION_819_fixed_f_coord_on_2',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_819_set_700C_to_pressed_button_3',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_819_add_4',
        "command": 'add',
        "args": [0x700c, 65516]
    },
    {
        "identifier": 'ACTION_819_load_mem_5',
        "command": 'load_mem',
        "args": [0x700c]
    },
    {
        "identifier": 'ACTION_819_pause_6',
        "command": 'pause',
        "args": [9]
    },
    {
        "identifier": 'ACTION_819_end_loop_7',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_819_set_sprite_sequence_8',
        "command": 'set_sprite_sequence',
        "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_819_pause_9',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'ACTION_819_set_sprite_sequence_10',
        "command": 'set_sprite_sequence',
        "args": [2, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_819_set_700C_to_pressed_button_11',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_819_add_12',
        "command": 'add',
        "args": [0x700c, 65515]
    },
    {
        "identifier": 'ACTION_819_add_13',
        "command": 'add',
        "args": [0x700c, 25]
    },
    {
        "identifier": 'ACTION_819_set_mem_704x_at_700C_bit_14',
        "command": 'set_mem_704x_at_700C_bit'
    },
    {
        "identifier": 'ACTION_819_add_15',
        "command": 'add',
        "args": [0x700c, 4]
    },
    {
        "identifier": 'ACTION_819_set_mem_704x_at_700C_bit_16',
        "command": 'set_mem_704x_at_700C_bit'
    },
    {
        "identifier": 'ACTION_819_pause_17',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'ACTION_819_set_700C_to_pressed_button_18',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_819_add_19',
        "command": 'add',
        "args": [0x700c, 65515]
    },
    {
        "identifier": 'ACTION_819_add_20',
        "command": 'add',
        "args": [0x700c, 25]
    },
    {
        "identifier": 'ACTION_819_clear_mem_704x_at_700C_bit_21',
        "command": 'clear_mem_704x_at_700C_bit'
    },
    {
        "identifier": 'ACTION_819_add_22',
        "command": 'add',
        "args": [0x700c, 4]
    },
    {
        "identifier": 'ACTION_819_clear_mem_704x_at_700C_bit_23',
        "command": 'clear_mem_704x_at_700C_bit'
    },
    {
        "identifier": 'ACTION_819_set_sprite_sequence_24',
        "command": 'set_sprite_sequence',
        "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_819_pause_25',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'ACTION_819_set_sprite_sequence_26',
        "command": 'set_sprite_sequence',
        "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_819_pause_27',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'ACTION_819_jmp_28',
        "command": 'jmp',
        "args": ['ACTION_819_set_sprite_sequence_8']
    }
]
