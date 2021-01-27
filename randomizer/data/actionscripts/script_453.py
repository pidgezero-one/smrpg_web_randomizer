from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_453_set_sprite_sequence_0',
        "command": 'set_sprite_sequence',
        "args": [6, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_453_jmp_if_bit_clear_1',
        "command": 'jmp_if_bit_clear',
        "args": [0x7045, 7, 'ACTION_453_pause_3']
    },
    {
        "identifier": 'ACTION_453_pause_2',
        "command": 'pause',
        "args": [176]
    },
    {
        "identifier": 'ACTION_453_pause_3',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_453_db_4',
        "command": 'db',
        "args": [0x3b, 0x00, 0x00, 0x04, 0xf4, 0x57]
    },
    {
        "identifier": 'ACTION_453_jmp_5',
        "command": 'jmp',
        "args": ['ACTION_453_pause_3']
    },
    {
        "identifier": 'ACTION_453_sequence_looping_on_6',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_453_set_sprite_sequence_7',
        "command": 'set_sprite_sequence',
        "args": [8, 0, [_0x08Flags.LOOPING_OFF]]
    },
    {
        "identifier": 'ACTION_453_pause_8',
        "command": 'pause',
        "args": [48]
    },
    {
        "identifier": 'ACTION_453_shift_northeast_steps_9',
        "command": 'shift_northeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_453_shift_northwest_steps_10',
        "command": 'shift_northwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_453_shift_southwest_steps_11',
        "command": 'shift_southwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_453_shift_southeast_steps_12',
        "command": 'shift_southeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_453_jmp_13',
        "command": 'jmp',
        "args": ['ACTION_453_shift_northeast_steps_9']
    }
]
