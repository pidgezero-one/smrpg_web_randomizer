from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_179_set_vram_priority_0',
        "command": 'set_vram_priority',
        "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
    },
    {
        "identifier": 'ACTION_179_set_sprite_sequence_1',
        "command": 'set_sprite_sequence',
        "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_179_pause_2',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'ACTION_179_set_sprite_sequence_3',
        "command": 'set_sprite_sequence',
        "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_179_pause_4',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'ACTION_179_set_sprite_sequence_5',
        "command": 'set_sprite_sequence',
        "args": [3, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_179_pause_6',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'ACTION_179_jmp_7',
        "command": 'jmp',
        "args": ['ACTION_179_set_sprite_sequence_1']
    }
]
