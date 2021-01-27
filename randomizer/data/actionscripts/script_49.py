from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_49_object_memory_set_bit_0',
        "command": 'object_memory_set_bit',
        "args": [0x0b, [3]]
    },
    {
        "identifier": 'ACTION_49_clear_solidity_bits_1',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_49_pause_2',
        "command": 'pause',
        "args": [13]
    },
    {
        "identifier": 'ACTION_49_inc_short_3',
        "command": 'inc_short',
        "args": [0x702c]
    },
    {
        "identifier": 'ACTION_49_walk_1_step_southwest_4',
        "command": 'walk_1_step_southwest'
    },
    {
        "identifier": 'ACTION_49_walk_1_step_southeast_5',
        "command": 'walk_1_step_southeast'
    },
    {
        "identifier": 'ACTION_49_shift_southwest_steps_6',
        "command": 'shift_southwest_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_49_shift_northwest_steps_7',
        "command": 'shift_northwest_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_49_jmp_if_random_above_128_8',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_49_shift_southeast_steps_13']
    },
    {
        "identifier": 'ACTION_49_shift_northeast_steps_9',
        "command": 'shift_northeast_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_49_shift_southeast_steps_10',
        "command": 'shift_southeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_49_walk_1_step_northeast_11',
        "command": 'walk_1_step_northeast'
    },
    {
        "identifier": 'ACTION_49_jmp_12',
        "command": 'jmp',
        "args": ['ACTION_49_object_memory_set_bit_0']
    },
    {
        "identifier": 'ACTION_49_shift_southeast_steps_13',
        "command": 'shift_southeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_49_shift_northeast_steps_14',
        "command": 'shift_northeast_steps',
        "args": [4]
    },
    {
        "identifier": 'ACTION_49_jmp_15',
        "command": 'jmp',
        "args": ['ACTION_49_object_memory_set_bit_0']
    }
]
