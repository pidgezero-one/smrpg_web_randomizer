from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_240_set_sprite_sequence_0',
        "command": 'set_sprite_sequence',
        "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_240_pause_1',
        "command": 'pause',
        "args": [45]
    },
    {
        "identifier": 'ACTION_240_play_sound_2',
        "command": 'play_sound',
        "args": [Sounds._145_BLACKSMITH_HAMMER_STRIKE, 4]
    },
    {
        "identifier": 'ACTION_240_set_bit_3',
        "command": 'set_bit',
        "args": [0x7044, 6]
    },
    {
        "identifier": 'ACTION_240_set_sprite_sequence_4',
        "command": 'set_sprite_sequence',
        "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_240_ret_5',
        "command": 'ret'
    }
]
