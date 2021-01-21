from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_776_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_776_shift_northwest_steps_1',
        "command": 'shift_northwest_steps',
        "args": [18]
    },
    {
        "identifier": 'ACTION_776_set_random_2',
        "command": 'set_random',
        "args": [0x700c, 16]
    },
    {
        "identifier": 'ACTION_776_add_3',
        "command": 'add',
        "args": [0x700c, 15]
    },
    {
        "identifier": 'ACTION_776_load_mem_4',
        "command": 'load_mem',
        "args": [0x700c]
    },
    {
        "identifier": 'ACTION_776_pause_5',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_776_end_loop_6',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_776_jmp_if_random_above_66_7',
        "command": 'jmp_if_random_above_66',
        "args": ['ACTION_776_set_animation_speed_14']
    },
    {
        "identifier": 'ACTION_776_pause_8',
        "command": 'pause',
        "args": [31]
    },
    {
        "identifier": 'ACTION_776_jmp_if_random_above_66_9',
        "command": 'jmp_if_random_above_66',
        "args": ['ACTION_776_set_animation_speed_14']
    },
    {
        "identifier": 'ACTION_776_set_animation_speed_10',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_776_shift_southeast_steps_11',
        "command": 'shift_southeast_steps',
        "args": [32]
    },
    {
        "identifier": 'ACTION_776_pause_12',
        "command": 'pause',
        "args": [51]
    },
    {
        "identifier": 'ACTION_776_jmp_13',
        "command": 'jmp',
        "args": ['ACTION_776_set_random_2']
    },
    {
        "identifier": 'ACTION_776_set_animation_speed_14',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_776_shift_south_steps_15',
        "command": 'shift_south_steps',
        "args": [16]
    },
    {
        "identifier": 'ACTION_776_pause_16',
        "command": 'pause',
        "args": [31]
    },
    {
        "identifier": 'ACTION_776_set_animation_speed_17',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_776_shift_northwest_steps_18',
        "command": 'shift_northwest_steps',
        "args": [32]
    },
    {
        "identifier": 'ACTION_776_pause_19',
        "command": 'pause',
        "args": [51]
    },
    {
        "identifier": 'ACTION_776_jmp_20',
        "command": 'jmp',
        "args": ['ACTION_776_set_random_2']
    }
]
