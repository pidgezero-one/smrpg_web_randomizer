from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_772_set_priority_0',
        "command": 'set_priority',
        "args": [2]
    },
    {
        "identifier": 'ACTION_772_set_sprite_sequence_1',
        "command": 'set_sprite_sequence',
        "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_772_clear_solidity_bits_2',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_772_sequence_looping_on_3',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_772_fixed_f_coord_on_4',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_772_set_700C_to_pressed_button_5',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_772_add_6',
        "command": 'add',
        "args": [0x700c, 65517]
    },
    {
        "identifier": 'ACTION_772_load_mem_7',
        "command": 'load_mem',
        "args": [0x700c]
    },
    {
        "identifier": 'ACTION_772_pause_8',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_772_end_loop_9',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_772_set_animation_speed_10',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_772_set_animation_speed_11',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_772_set_random_12',
        "command": 'set_random',
        "args": [0x700c, 12]
    },
    {
        "identifier": 'ACTION_772_add_short_13',
        "command": 'add_short',
        "args": [0x700c, 0x01]
    },
    {
        "identifier": 'ACTION_772_load_mem_14',
        "command": 'load_mem',
        "args": [0x700c]
    },
    {
        "identifier": 'ACTION_772_pause_15',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'ACTION_772_end_loop_16',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_772_set_sprite_sequence_17',
        "command": 'set_sprite_sequence',
        "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_772_shift_northwest_steps_18',
        "command": 'shift_northwest_steps',
        "args": [4]
    },
    {
        "identifier": 'ACTION_772_shift_southeast_steps_19',
        "command": 'shift_southeast_steps',
        "args": [4]
    },
    {
        "identifier": 'ACTION_772_jmp_20',
        "command": 'jmp',
        "args": ['ACTION_772_set_random_12']
    }
]
