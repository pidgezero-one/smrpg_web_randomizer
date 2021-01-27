from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_408_set_700C_to_object_coord_0',
        "command": 'set_700C_to_object_coord',
        "args": [AreaObjects.MARIO, Coords.F, []]
    },
    {
        "identifier": 'ACTION_408_jmp_if_700C_equals_short_1',
        "command": 'jmp_if_700C_equals_short',
        "args": [0, 'ACTION_408_set_sprite_sequence_10']
    },
    {
        "identifier": 'ACTION_408_jmp_if_700C_equals_short_2',
        "command": 'jmp_if_700C_equals_short',
        "args": [1, 'ACTION_408_set_sprite_sequence_12']
    },
    {
        "identifier": 'ACTION_408_jmp_if_700C_equals_short_3',
        "command": 'jmp_if_700C_equals_short',
        "args": [2, 'ACTION_408_set_sprite_sequence_14']
    },
    {
        "identifier": 'ACTION_408_jmp_if_700C_equals_short_4',
        "command": 'jmp_if_700C_equals_short',
        "args": [3, 'ACTION_408_set_sprite_sequence_16']
    },
    {
        "identifier": 'ACTION_408_jmp_if_700C_equals_short_5',
        "command": 'jmp_if_700C_equals_short',
        "args": [4, 'ACTION_408_set_sprite_sequence_18']
    },
    {
        "identifier": 'ACTION_408_jmp_if_700C_equals_short_6',
        "command": 'jmp_if_700C_equals_short',
        "args": [5, 'ACTION_408_set_sprite_sequence_20']
    },
    {
        "identifier": 'ACTION_408_jmp_if_700C_equals_short_7',
        "command": 'jmp_if_700C_equals_short',
        "args": [6, 'ACTION_408_set_sprite_sequence_22']
    },
    {
        "identifier": 'ACTION_408_set_sprite_sequence_8',
        "command": 'set_sprite_sequence',
        "args": [4, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_408_jmp_9',
        "command": 'jmp',
        "args": ['ACTION_408_ret_23']
    },
    {
        "identifier": 'ACTION_408_set_sprite_sequence_10',
        "command": 'set_sprite_sequence',
        "args": [2, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_408_jmp_11',
        "command": 'jmp',
        "args": ['ACTION_408_ret_23']
    },
    {
        "identifier": 'ACTION_408_set_sprite_sequence_12',
        "command": 'set_sprite_sequence',
        "args": [3, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_408_jmp_13',
        "command": 'jmp',
        "args": ['ACTION_408_ret_23']
    },
    {
        "identifier": 'ACTION_408_set_sprite_sequence_14',
        "command": 'set_sprite_sequence',
        "args": [0, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_408_jmp_15',
        "command": 'jmp',
        "args": ['ACTION_408_ret_23']
    },
    {
        "identifier": 'ACTION_408_set_sprite_sequence_16',
        "command": 'set_sprite_sequence',
        "args": [3, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_408_jmp_17',
        "command": 'jmp',
        "args": ['ACTION_408_ret_23']
    },
    {
        "identifier": 'ACTION_408_set_sprite_sequence_18',
        "command": 'set_sprite_sequence',
        "args": [2, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_408_jmp_19',
        "command": 'jmp',
        "args": ['ACTION_408_ret_23']
    },
    {
        "identifier": 'ACTION_408_set_sprite_sequence_20',
        "command": 'set_sprite_sequence',
        "args": [4, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_408_jmp_21',
        "command": 'jmp',
        "args": ['ACTION_408_ret_23']
    },
    {
        "identifier": 'ACTION_408_set_sprite_sequence_22',
        "command": 'set_sprite_sequence',
        "args": [1, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_408_ret_23',
        "command": 'ret'
    }
]
