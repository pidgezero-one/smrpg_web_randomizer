from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_17_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_17_set_sprite_sequence_1',
        "command": 'set_sprite_sequence',
        "args": [6, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_17_shift_northwest_pixels_2',
        "command": 'shift_northwest_pixels',
        "args": [1]
    },
    {
        "identifier": 'ACTION_17_shift_southeast_pixels_3',
        "command": 'shift_southeast_pixels',
        "args": [2]
    },
    {
        "identifier": 'ACTION_17_shift_northwest_pixels_4',
        "command": 'shift_northwest_pixels',
        "args": [1]
    },
    {
        "identifier": 'ACTION_17_start_loop_n_times_5',
        "command": 'start_loop_n_times',
        "args": [29]
    },
    {
        "identifier": 'ACTION_17_jmp_if_bit_set_6',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 2, 'ACTION_17_face_southeast_10']
    },
    {
        "identifier": 'ACTION_17_pause_7',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_17_end_loop_8',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_17_jmp_9',
        "command": 'jmp',
        "args": ['ACTION_17_shift_northwest_pixels_2']
    },
    {
        "identifier": 'ACTION_17_face_southeast_10',
        "command": 'face_southeast'
    },
    {
        "identifier": 'ACTION_17_set_animation_speed_11',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_17_reset_properties_12',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_17_ret_13',
        "command": 'ret'
    }
]
