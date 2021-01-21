from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_455_set_sprite_sequence_0',
        "command": 'set_sprite_sequence',
        "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_455_set_bit_1',
        "command": 'set_bit',
        "args": [0x7045, 0]
    },
    {
        "identifier": 'ACTION_455_clear_bit_2',
        "command": 'clear_bit',
        "args": [0x7045, 2]
    },
    {
        "identifier": 'ACTION_455_pause_3',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'ACTION_455_set_sprite_sequence_4',
        "command": 'set_sprite_sequence',
        "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_455_set_bit_5',
        "command": 'set_bit',
        "args": [0x7045, 1]
    },
    {
        "identifier": 'ACTION_455_clear_bit_6',
        "command": 'clear_bit',
        "args": [0x7045, 0]
    },
    {
        "identifier": 'ACTION_455_pause_7',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'ACTION_455_set_sprite_sequence_8',
        "command": 'set_sprite_sequence',
        "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_455_set_bit_9',
        "command": 'set_bit',
        "args": [0x7045, 0]
    },
    {
        "identifier": 'ACTION_455_clear_bit_10',
        "command": 'clear_bit',
        "args": [0x7045, 1]
    },
    {
        "identifier": 'ACTION_455_pause_11',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'ACTION_455_set_sprite_sequence_12',
        "command": 'set_sprite_sequence',
        "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_455_set_bit_13',
        "command": 'set_bit',
        "args": [0x7045, 2]
    },
    {
        "identifier": 'ACTION_455_clear_bit_14',
        "command": 'clear_bit',
        "args": [0x7045, 0]
    },
    {
        "identifier": 'ACTION_455_pause_15',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'ACTION_455_jmp_16',
        "command": 'jmp',
        "args": ['ACTION_455_set_sprite_sequence_0']
    }
]
