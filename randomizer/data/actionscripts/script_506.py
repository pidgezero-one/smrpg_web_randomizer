from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_506_set_sprite_sequence_0',
        "command": 'set_sprite_sequence',
        "args": [22, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_506_pause_1',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_506_set_sprite_sequence_2',
        "command": 'set_sprite_sequence',
        "args": [31, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_506_pause_3',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'ACTION_506_set_sprite_sequence_4',
        "command": 'set_sprite_sequence',
        "args": [22, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_506_pause_5',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'ACTION_506_set_sprite_sequence_6',
        "command": 'set_sprite_sequence',
        "args": [3, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_506_pause_7',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_506_jmp_8',
        "command": 'jmp',
        "args": ['ACTION_506_set_sprite_sequence_0']
    }
]
