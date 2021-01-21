from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_717_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_717_shift_northwest_steps_1',
        "command": 'shift_northwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_717_fixed_f_coord_on_2',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_717_jmp_if_random_above_66_3',
        "command": 'jmp_if_random_above_66',
        "args": ['ACTION_717_pause_6']
    },
    {
        "identifier": 'ACTION_717_pause_4',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_717_jmp_5',
        "command": 'jmp',
        "args": ['ACTION_717_jmp_if_random_above_66_3']
    },
    {
        "identifier": 'ACTION_717_pause_6',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_717_shift_northeast_steps_7',
        "command": 'shift_northeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_717_jmp_8',
        "command": 'jmp',
        "args": ['ACTION_717_jmp_if_random_above_128_12']
    },
    {
        "identifier": 'ACTION_717_pause_9',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_717_shift_southwest_steps_10',
        "command": 'shift_southwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_717_jmp_11',
        "command": 'jmp',
        "args": ['ACTION_717_jmp_if_random_above_128_17']
    },
    {
        "identifier": 'ACTION_717_jmp_if_random_above_128_12',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_717_pause_14']
    },
    {
        "identifier": 'ACTION_717_pause_13',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_717_pause_14',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_717_shift_southwest_steps_15',
        "command": 'shift_southwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_717_jmp_16',
        "command": 'jmp',
        "args": ['ACTION_717_jmp_if_random_above_66_3']
    },
    {
        "identifier": 'ACTION_717_jmp_if_random_above_128_17',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_717_pause_19']
    },
    {
        "identifier": 'ACTION_717_pause_18',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_717_pause_19',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_717_shift_northeast_steps_20',
        "command": 'shift_northeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_717_jmp_21',
        "command": 'jmp',
        "args": ['ACTION_717_jmp_if_random_above_66_3']
    }
]
