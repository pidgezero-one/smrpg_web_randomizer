from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_155_fixed_f_coord_off_0',
        "command": 'fixed_f_coord_off'
    },
    {
        "identifier": 'ACTION_155_set_sprite_sequence_1',
        "command": 'set_sprite_sequence',
        "args": [10, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_155_pause_2',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'ACTION_155_set_sprite_sequence_3',
        "command": 'set_sprite_sequence',
        "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_155_jmp_4',
        "command": 'jmp',
        "args": ['ACTION_154_fixed_f_coord_on_0']
    },
    {
        "identifier": 'ACTION_155_ret_5',
        "command": 'ret'
    }
]
