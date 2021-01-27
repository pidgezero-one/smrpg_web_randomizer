from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_428_set_sprite_sequence_0',
        "command": 'set_sprite_sequence',
        "args": [5, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_428_set_object_memory_bits_1',
        "command": 'set_object_memory_bits',
        "args": [0x0e, [2, 3]]
    },
    {
        "identifier": 'ACTION_428_pause_2',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_428_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 2, 'ACTION_431_set_animation_speed_0']
    },
    {
        "identifier": 'ACTION_428_jmp_4',
        "command": 'jmp',
        "args": ['ACTION_428_pause_2']
    }
]
