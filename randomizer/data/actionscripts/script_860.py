from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_860_face_northeast_0',
        "command": 'face_northeast'
    },
    {
        "identifier": 'ACTION_860_set_sprite_sequence_1',
        "command": 'set_sprite_sequence',
        "args": [4, inc_sprite=1, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_860_set_priority_2',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_860_db_3',
        "command": 'db',
        "args": [0x20, 0x07]
    },
    {
        "identifier": 'ACTION_860_db_4',
        "command": 'db',
        "args": [0x24, 0x20, 0x01, 0xc0, 0xfe]
    },
    {
        "identifier": 'ACTION_860_db_5',
        "command": 'db',
        "args": [0x25, 0x00, 0x0e, 0x80, 0xff]
    },
    {
        "identifier": 'ACTION_860_pause_6',
        "command": 'pause',
        "args": [46]
    },
    {
        "identifier": 'ACTION_860_bpl_26_27_28_7',
        "command": 'bpl_26_27_28'
    },
    {
        "identifier": 'ACTION_860_play_sound_8',
        "command": 'play_sound',
        "args": [Sounds._058_INSERT, 4]
    },
    {
        "identifier": 'ACTION_860_overwrite_solidity_9',
        "command": 'overwrite_solidity',
        "args": [[_0x0AFlags.CANT_PASS_WALLS, _0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_860_ret_10',
        "command": 'ret'
    }
]
