from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_413_sequence_looping_on_0',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_413_pause_1',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_413_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 6, 'ACTION_413_sequence_looping_off_4']
    },
    {
        "identifier": 'ACTION_413_jmp_3',
        "command": 'jmp',
        "args": ['ACTION_413_sequence_looping_on_0']
    },
    {
        "identifier": 'ACTION_413_sequence_looping_off_4',
        "command": 'sequence_looping_off'
    },
    {
        "identifier": 'ACTION_413_pause_5',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'ACTION_413_jmp_if_bit_clear_6',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 5, 'ACTION_413_sequence_looping_off_4']
    },
    {
        "identifier": 'ACTION_413_jmp_7',
        "command": 'jmp',
        "args": ['ACTION_413_sequence_looping_on_0']
    }
]
