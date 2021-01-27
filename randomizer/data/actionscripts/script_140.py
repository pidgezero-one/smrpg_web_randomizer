from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_140_start_loop_n_times_0',
        "command": 'start_loop_n_times',
        "args": [1]
    },
    {
        "identifier": 'ACTION_140_set_sprite_sequence_1',
        "command": 'set_sprite_sequence',
        "args": [30, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_140_pause_2',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'ACTION_140_set_sprite_sequence_3',
        "command": 'set_sprite_sequence',
        "args": [27, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_140_pause_4',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'ACTION_140_end_loop_5',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_140_set_sprite_sequence_6',
        "command": 'set_sprite_sequence',
        "args": [30, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_140_pause_7',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'ACTION_140_jmp_8',
        "command": 'jmp',
        "args": ['ACTION_140_start_loop_n_times_0']
    }
]
