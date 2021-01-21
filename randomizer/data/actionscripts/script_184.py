from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_184_set_vram_priority_0',
        "command": 'set_vram_priority',
        "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
    },
    {
        "identifier": 'ACTION_184_set_priority_1',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_184_set_2',
        "command": 'set',
        "args": [0x70c0, 1]
    },
    {
        "identifier": 'ACTION_184_set_sprite_sequence_3',
        "command": 'set_sprite_sequence',
        "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_184_pause_4',
        "command": 'pause',
        "args": [9]
    },
    {
        "identifier": 'ACTION_184_set_5',
        "command": 'set',
        "args": [0x70c0, 0]
    },
    {
        "identifier": 'ACTION_184_set_sprite_sequence_6',
        "command": 'set_sprite_sequence',
        "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_184_pause_7',
        "command": 'pause',
        "args": [9]
    },
    {
        "identifier": 'ACTION_184_set_8',
        "command": 'set',
        "args": [0x70c0, 2]
    },
    {
        "identifier": 'ACTION_184_set_sprite_sequence_9',
        "command": 'set_sprite_sequence',
        "args": [3, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_184_pause_10',
        "command": 'pause',
        "args": [9]
    },
    {
        "identifier": 'ACTION_184_jmp_11',
        "command": 'jmp',
        "args": ['ACTION_184_set_2']
    }
]
