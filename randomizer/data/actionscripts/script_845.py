from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_845_set_sprite_sequence_0',
        "command": 'set_sprite_sequence',
        "args": [4, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_845_visibility_on_1',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_845_pause_2',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'ACTION_845_jmp_if_random_above_128_3',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_845_set_sprite_sequence_6']
    },
    {
        "identifier": 'ACTION_845_set_sprite_sequence_4',
        "command": 'set_sprite_sequence',
        "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_845_jmp_5',
        "command": 'jmp',
        "args": ['ACTION_845_pause_7']
    },
    {
        "identifier": 'ACTION_845_set_sprite_sequence_6',
        "command": 'set_sprite_sequence',
        "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_845_pause_7',
        "command": 'pause',
        "args": [48]
    },
    {
        "identifier": 'ACTION_845_jmp_if_random_above_128_8',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_845_start_loop_n_times_22']
    },
    {
        "identifier": 'ACTION_845_start_loop_n_times_9',
        "command": 'start_loop_n_times',
        "args": [2]
    },
    {
        "identifier": 'ACTION_845_set_sprite_sequence_10',
        "command": 'set_sprite_sequence',
        "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_845_pause_11',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_845_set_sprite_sequence_12',
        "command": 'set_sprite_sequence',
        "args": [1, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_845_pause_13',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'ACTION_845_set_sprite_sequence_14',
        "command": 'set_sprite_sequence',
        "args": [2, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_845_pause_15',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_845_set_sprite_sequence_16',
        "command": 'set_sprite_sequence',
        "args": [1, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_845_pause_17',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_845_set_sprite_sequence_18',
        "command": 'set_sprite_sequence',
        "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_845_pause_19',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'ACTION_845_end_loop_20',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_845_jmp_21',
        "command": 'jmp',
        "args": ['ACTION_845_jmp_if_random_above_128_8']
    },
    {
        "identifier": 'ACTION_845_start_loop_n_times_22',
        "command": 'start_loop_n_times',
        "args": [2]
    },
    {
        "identifier": 'ACTION_845_set_sprite_sequence_23',
        "command": 'set_sprite_sequence',
        "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_845_pause_24',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_845_set_sprite_sequence_25',
        "command": 'set_sprite_sequence',
        "args": [1, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_845_pause_26',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'ACTION_845_set_sprite_sequence_27',
        "command": 'set_sprite_sequence',
        "args": [2, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_845_pause_28',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_845_set_sprite_sequence_29',
        "command": 'set_sprite_sequence',
        "args": [1, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_845_pause_30',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_845_set_sprite_sequence_31',
        "command": 'set_sprite_sequence',
        "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_845_pause_32',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'ACTION_845_end_loop_33',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_845_jmp_34',
        "command": 'jmp',
        "args": ['ACTION_845_jmp_if_random_above_128_8']
    }
]
