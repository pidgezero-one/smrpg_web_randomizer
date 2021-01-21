from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_493_set_priority_0',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_493_set_sprite_sequence_1',
        "command": 'set_sprite_sequence',
        "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_493_pause_2',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'ACTION_493_set_priority_3',
        "command": 'set_priority',
        "args": [0]
    },
    {
        "identifier": 'ACTION_493_pause_4',
        "command": 'pause',
        "args": [192]
    },
    {
        "identifier": 'ACTION_493_jmp_5',
        "command": 'jmp',
        "args": ['ACTION_493_set_priority_0']
    }
]
