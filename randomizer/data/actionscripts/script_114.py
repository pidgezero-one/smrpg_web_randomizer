from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_114_set_sprite_sequence_0',
        "command": 'set_sprite_sequence',
        "args": [14, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_114_pause_1',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'ACTION_114_set_sprite_sequence_2',
        "command": 'set_sprite_sequence',
        "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_114_pause_3',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'ACTION_114_jmp_4',
        "command": 'jmp',
        "args": ['ACTION_114_set_sprite_sequence_0']
    }
]
