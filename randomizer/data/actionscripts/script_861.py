from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_861_set_sprite_sequence_0',
        "command": 'set_sprite_sequence',
        "args": [0, 3, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_861_pause_1',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'ACTION_861_set_sprite_sequence_2',
        "command": 'set_sprite_sequence',
        "args": [0, 3, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_861_pause_3',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'ACTION_861_jmp_4',
        "command": 'jmp',
        "args": ['ACTION_861_set_sprite_sequence_0']
    }
]
