from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_645_set_priority_0',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_645_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7078, 3, 'ACTION_645_clear_bit_13']
    },
    {
        "identifier": 'ACTION_645_pause_2',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_645_jmp_if_bit_clear_3',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 2, 'ACTION_645_pause_2']
    },
    {
        "identifier": 'ACTION_645_pause_4',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_645_jmp_if_bit_set_5',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 2, 'ACTION_645_pause_4']
    },
    {
        "identifier": 'ACTION_645_pause_6',
        "command": 'pause',
        "args": [109]
    },
    {
        "identifier": 'ACTION_645_start_loop_n_times_7',
        "command": 'start_loop_n_times',
        "args": [1]
    },
    {
        "identifier": 'ACTION_645_pause_8',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'ACTION_645_set_sprite_sequence_9',
        "command": 'set_sprite_sequence',
        "args": [3, 0, [_0x08Flags.LOOPING_OFF]]
    },
    {
        "identifier": 'ACTION_645_pause_10',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'ACTION_645_end_loop_11',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_645_ret_12',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_645_clear_bit_13',
        "command": 'clear_bit',
        "args": [0x707b, 5]
    },
    {
        "identifier": 'ACTION_645_pause_14',
        "command": 'pause',
        "args": [168]
    },
    {
        "identifier": 'ACTION_645_set_sprite_sequence_15',
        "command": 'set_sprite_sequence',
        "args": [3, 0, [_0x08Flags.LOOPING_OFF]]
    },
    {
        "identifier": 'ACTION_645_pause_16',
        "command": 'pause',
        "args": [64]
    },
    {
        "identifier": 'ACTION_645_jmp_if_bit_set_17',
        "command": 'jmp_if_bit_set',
        "args": [0x7078, 5, 'ACTION_645_pause_22']
    },
    {
        "identifier": 'ACTION_645_set_sprite_sequence_18',
        "command": 'set_sprite_sequence',
        "args": [3, 0, [_0x08Flags.LOOPING_OFF]]
    },
    {
        "identifier": 'ACTION_645_pause_19',
        "command": 'pause',
        "args": [35]
    },
    {
        "identifier": 'ACTION_645_set_bit_20',
        "command": 'set_bit',
        "args": [0x707b, 5]
    },
    {
        "identifier": 'ACTION_645_ret_21',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_645_pause_22',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'ACTION_645_set_sprite_sequence_23',
        "command": 'set_sprite_sequence',
        "args": [3, 0, [_0x08Flags.LOOPING_OFF]]
    },
    {
        "identifier": 'ACTION_645_pause_24',
        "command": 'pause',
        "args": [36]
    },
    {
        "identifier": 'ACTION_645_set_animation_speed_25',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_645_set_sprite_sequence_26',
        "command": 'set_sprite_sequence',
        "args": [2, 0, [_0x08Flags.LOOPING_OFF]]
    },
    {
        "identifier": 'ACTION_645_pause_27',
        "command": 'pause',
        "args": [50]
    },
    {
        "identifier": 'ACTION_645_face_southeast_28',
        "command": 'face_southeast'
    },
    {
        "identifier": 'ACTION_645_pause_29',
        "command": 'pause',
        "args": [40]
    },
    {
        "identifier": 'ACTION_645_set_sprite_sequence_30',
        "command": 'set_sprite_sequence',
        "args": [4, 0, [_0x08Flags.LOOPING_OFF, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_645_ret_31',
        "command": 'ret'
    }
]
