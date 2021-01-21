from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_766_pause_0',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'ACTION_766_set_sprite_sequence_1',
        "command": 'set_sprite_sequence',
        "args": [7, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_766_pause_2',
        "command": 'pause',
        "args": [56]
    },
    {
        "identifier": 'ACTION_766_set_sprite_sequence_3',
        "command": 'set_sprite_sequence',
        "args": [10, inc_sprite=4, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_766_pause_4',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_766_set_sprite_sequence_5',
        "command": 'set_sprite_sequence',
        "args": [9, inc_sprite=4, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_766_pause_6',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_766_jmp_7',
        "command": 'jmp',
        "args": ['ACTION_766_set_sprite_sequence_3']
    }
]
