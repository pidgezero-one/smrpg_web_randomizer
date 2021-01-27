from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_414_face_northwest_0',
        "command": 'face_northwest'
    },
    {
        "identifier": 'ACTION_414_set_sprite_sequence_1',
        "command": 'set_sprite_sequence',
        "args": [4, 1, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_414_set_priority_2',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_414_db_3',
        "command": 'db',
        "args": [0x20, 0x07]
    },
    {
        "identifier": 'ACTION_414_db_4',
        "command": 'db',
        "args": [0x24, 0x00, 0xfe, 0x00, 0xff]
    },
    {
        "identifier": 'ACTION_414_db_5',
        "command": 'db',
        "args": [0x25, 0x00, 0x0f, 0x80, 0xff]
    },
    {
        "identifier": 'ACTION_414_pause_6',
        "command": 'pause',
        "args": [46]
    },
    {
        "identifier": 'ACTION_414_bpl_26_27_28_7',
        "command": 'bpl_26_27_28'
    },
    {
        "identifier": 'ACTION_414_play_sound_8',
        "command": 'play_sound',
        "args": [Sounds._058_INSERT, 4]
    },
    {
        "identifier": 'ACTION_414_overwrite_solidity_9',
        "command": 'overwrite_solidity',
        "args": [[_0x0AFlags.CANT_PASS_WALLS, _0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_414_ret_10',
        "command": 'ret'
    }
]
