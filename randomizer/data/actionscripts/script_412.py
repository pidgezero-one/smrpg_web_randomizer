from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_412_set_priority_0',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_412_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_412_sequence_looping_on_2',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_412_db_3',
        "command": 'db',
        "args": [0x20, 0x07]
    },
    {
        "identifier": 'ACTION_412_jmp_if_random_above_128_4',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_412_embedded_animation_routine_7']
    },
    {
        "identifier": 'ACTION_412_embedded_animation_routine_5',
        "command": 'embedded_animation_routine',
        "args": [0x26]
    },
    {
        "identifier": 'ACTION_412_jmp_6',
        "command": 'jmp',
        "args": ['ACTION_412_jmp_if_random_above_128_8']
    },
    {
        "identifier": 'ACTION_412_embedded_animation_routine_7',
        "command": 'embedded_animation_routine',
        "args": [0x26]
    },
    {
        "identifier": 'ACTION_412_jmp_if_random_above_128_8',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_412_embedded_animation_routine_11']
    },
    {
        "identifier": 'ACTION_412_embedded_animation_routine_9',
        "command": 'embedded_animation_routine',
        "args": [0x27]
    },
    {
        "identifier": 'ACTION_412_jmp_10',
        "command": 'jmp',
        "args": ['ACTION_412_jmp_if_random_above_128_12']
    },
    {
        "identifier": 'ACTION_412_embedded_animation_routine_11',
        "command": 'embedded_animation_routine',
        "args": [0x27]
    },
    {
        "identifier": 'ACTION_412_jmp_if_random_above_128_12',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_412_embedded_animation_routine_15']
    },
    {
        "identifier": 'ACTION_412_embedded_animation_routine_13',
        "command": 'embedded_animation_routine',
        "args": [0x28]
    },
    {
        "identifier": 'ACTION_412_jmp_14',
        "command": 'jmp',
        "args": ['ACTION_412_db_16']
    },
    {
        "identifier": 'ACTION_412_embedded_animation_routine_15',
        "command": 'embedded_animation_routine',
        "args": [0x28]
    },
    {
        "identifier": 'ACTION_412_db_16',
        "command": 'db',
        "args": [0x3b, 0x00, 0x80, 0x04, 0xb1, 0x4c]
    },
    {
        "identifier": 'ACTION_412_pause_17',
        "command": 'pause',
        "args": [48]
    },
    {
        "identifier": 'ACTION_412_jmp_18',
        "command": 'jmp',
        "args": ['ACTION_412_db_16']
    },
    {
        "identifier": 'ACTION_412_bpl_26_27_28_19',
        "command": 'bpl_26_27_28'
    },
    {
        "identifier": 'ACTION_412_clear_solidity_bits_20',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_412_set_priority_21',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_412_db_22',
        "command": 'db',
        "args": [0x20, 0x07]
    },
    {
        "identifier": 'ACTION_412_bpl_26_27_23',
        "command": 'bpl_26_27'
    },
    {
        "identifier": 'ACTION_412_visibility_on_24',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_412_db_25',
        "command": 'db',
        "args": [0x30, 0x00, 0x02]
    },
    {
        "identifier": 'ACTION_412_db_26',
        "command": 'db',
        "args": [0x29, 0x00]
    },
    {
        "identifier": 'ACTION_412_pause_27',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_412_jmp_28',
        "command": 'jmp',
        "args": ['ACTION_412_pause_27']
    }
]
