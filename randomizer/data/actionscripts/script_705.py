from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_705_set_random_0',
        "command": 'set_random',
        "args": [0x700c, 16]
    },
    {
        "identifier": 'ACTION_705_add_1',
        "command": 'add',
        "args": [0x700c, 15]
    },
    {
        "identifier": 'ACTION_705_load_mem_2',
        "command": 'load_mem',
        "args": [0x700c]
    },
    {
        "identifier": 'ACTION_705_pause_3',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_705_end_loop_4',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_705_jmp_if_random_above_66_5',
        "command": 'jmp_if_random_above_66',
        "args": ['ACTION_705_set_animation_speed_14']
    },
    {
        "identifier": 'ACTION_705_pause_6',
        "command": 'pause',
        "args": [31]
    },
    {
        "identifier": 'ACTION_705_jmp_if_random_above_66_7',
        "command": 'jmp_if_random_above_66',
        "args": ['ACTION_705_set_animation_speed_14']
    },
    {
        "identifier": 'ACTION_705_set_animation_speed_8',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_705_jmp_if_bit_set_9',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 4, 'ACTION_705_ret_25']
    },
    {
        "identifier": 'ACTION_705_shift_southeast_steps_10',
        "command": 'shift_southeast_steps',
        "args": [32]
    },
    {
        "identifier": 'ACTION_705_jmp_if_bit_set_11',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 4, 'ACTION_705_ret_25']
    },
    {
        "identifier": 'ACTION_705_pause_12',
        "command": 'pause',
        "args": [71]
    },
    {
        "identifier": 'ACTION_705_jmp_13',
        "command": 'jmp',
        "args": ['ACTION_705_set_random_0']
    },
    {
        "identifier": 'ACTION_705_set_animation_speed_14',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_705_jmp_if_bit_set_15',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 4, 'ACTION_705_ret_25']
    },
    {
        "identifier": 'ACTION_705_shift_south_steps_16',
        "command": 'shift_south_steps',
        "args": [16]
    },
    {
        "identifier": 'ACTION_705_jmp_if_bit_set_17',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 4, 'ACTION_705_ret_25']
    },
    {
        "identifier": 'ACTION_705_pause_18',
        "command": 'pause',
        "args": [41]
    },
    {
        "identifier": 'ACTION_705_set_animation_speed_19',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_705_jmp_if_bit_set_20',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 4, 'ACTION_705_ret_25']
    },
    {
        "identifier": 'ACTION_705_shift_northwest_steps_21',
        "command": 'shift_northwest_steps',
        "args": [32]
    },
    {
        "identifier": 'ACTION_705_jmp_if_bit_set_22',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 4, 'ACTION_705_ret_25']
    },
    {
        "identifier": 'ACTION_705_pause_23',
        "command": 'pause',
        "args": [71]
    },
    {
        "identifier": 'ACTION_705_jmp_24',
        "command": 'jmp',
        "args": ['ACTION_705_set_random_0']
    },
    {
        "identifier": 'ACTION_705_ret_25',
        "command": 'ret'
    }
]
