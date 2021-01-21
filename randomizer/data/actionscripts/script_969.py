from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_969_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_969_walk_1_step_northwest_1',
        "command": 'walk_1_step_northwest'
    },
    {
        "identifier": 'ACTION_969_walk_1_step_northeast_2',
        "command": 'walk_1_step_northeast'
    },
    {
        "identifier": 'ACTION_969_start_loop_n_times_3',
        "command": 'start_loop_n_times',
        "args": [5]
    },
    {
        "identifier": 'ACTION_969_set_sprite_sequence_4',
        "command": 'set_sprite_sequence',
        "args": [4, inc_sprite=2, flags=[_0x08Flags.LOOPING_OFF]]
    },
    {
        "identifier": 'ACTION_969_pause_5',
        "command": 'pause',
        "args": [46]
    },
    {
        "identifier": 'ACTION_969_end_loop_6',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_969_set_sprite_sequence_7',
        "command": 'set_sprite_sequence',
        "args": [13, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_969_pause_8',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'ACTION_969_set_sprite_sequence_9',
        "command": 'set_sprite_sequence',
        "args": [18, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_969_pause_10',
        "command": 'pause',
        "args": [56]
    },
    {
        "identifier": 'ACTION_969_reset_properties_11',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_969_set_animation_speed_12',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_969_set_animation_speed_13',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_969_shift_southwest_steps_14',
        "command": 'shift_southwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_969_shift_southwest_pixels_15',
        "command": 'shift_southwest_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_969_walk_1_step_northwest_16',
        "command": 'walk_1_step_northwest'
    },
    {
        "identifier": 'ACTION_969_pause_17',
        "command": 'pause',
        "args": [64]
    },
    {
        "identifier": 'ACTION_969_set_animation_speed_18',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_969_set_sprite_sequence_19',
        "command": 'set_sprite_sequence',
        "args": [5, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_969_ret_20',
        "command": 'ret'
    }
]
