from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_76_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 1, 'ACTION_76_set_sprite_sequence_6']
    },
    {
        "identifier": 'ACTION_76_set_sprite_sequence_1',
        "command": 'set_sprite_sequence',
        "args": [14, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_76_pause_2',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_76_set_sprite_sequence_3',
        "command": 'set_sprite_sequence',
        "args": [21, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_76_pause_4',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'ACTION_76_jmp_5',
        "command": 'jmp',
        "args": ['ACTION_76_set_sprite_sequence_1']
    },
    {
        "identifier": 'ACTION_76_set_sprite_sequence_6',
        "command": 'set_sprite_sequence',
        "args": [14, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_76_pause_7',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'ACTION_76_set_sprite_sequence_8',
        "command": 'set_sprite_sequence',
        "args": [21, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_76_pause_9',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_76_jmp_10',
        "command": 'jmp',
        "args": ['ACTION_76_set_sprite_sequence_6']
    }
]
