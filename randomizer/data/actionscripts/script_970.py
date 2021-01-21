from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_970_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_970_walk_1_step_northwest_1',
        "command": 'walk_1_step_northwest'
    },
    {
        "identifier": 'ACTION_970_shift_northwest_pixels_2',
        "command": 'shift_northwest_pixels',
        "args": [4]
    },
    {
        "identifier": 'ACTION_970_face_northeast_3',
        "command": 'face_northeast'
    },
    {
        "identifier": 'ACTION_970_set_700C_to_pressed_button_4',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_970_jmp_if_var_equals_short_5',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 21, 'ACTION_970_start_loop_n_times_15']
    },
    {
        "identifier": 'ACTION_970_jmp_if_var_equals_short_6',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 22, 'ACTION_970_start_loop_n_times_23']
    },
    {
        "identifier": 'ACTION_970_start_loop_n_times_7',
        "command": 'start_loop_n_times',
        "args": [9]
    },
    {
        "identifier": 'ACTION_970_set_sprite_sequence_8',
        "command": 'set_sprite_sequence',
        "args": [3, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_970_pause_9',
        "command": 'pause',
        "args": [34]
    },
    {
        "identifier": 'ACTION_970_end_loop_10',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_970_set_sprite_sequence_11',
        "command": 'set_sprite_sequence',
        "args": [4, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_970_pause_12',
        "command": 'pause',
        "args": [80]
    },
    {
        "identifier": 'ACTION_970_set_sprite_sequence_13',
        "command": 'set_sprite_sequence',
        "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_970_ret_14',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_970_start_loop_n_times_15',
        "command": 'start_loop_n_times',
        "args": [10]
    },
    {
        "identifier": 'ACTION_970_set_sprite_sequence_16',
        "command": 'set_sprite_sequence',
        "args": [3, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_970_pause_17',
        "command": 'pause',
        "args": [34]
    },
    {
        "identifier": 'ACTION_970_end_loop_18',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_970_set_sprite_sequence_19',
        "command": 'set_sprite_sequence',
        "args": [4, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_970_pause_20',
        "command": 'pause',
        "args": [64]
    },
    {
        "identifier": 'ACTION_970_set_sprite_sequence_21',
        "command": 'set_sprite_sequence',
        "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_970_ret_22',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_970_start_loop_n_times_23',
        "command": 'start_loop_n_times',
        "args": [11]
    },
    {
        "identifier": 'ACTION_970_set_sprite_sequence_24',
        "command": 'set_sprite_sequence',
        "args": [3, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_970_pause_25',
        "command": 'pause',
        "args": [34]
    },
    {
        "identifier": 'ACTION_970_end_loop_26',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_970_set_sprite_sequence_27',
        "command": 'set_sprite_sequence',
        "args": [4, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_970_pause_28',
        "command": 'pause',
        "args": [48]
    },
    {
        "identifier": 'ACTION_970_set_sprite_sequence_29',
        "command": 'set_sprite_sequence',
        "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_970_ret_30',
        "command": 'ret'
    }
]
