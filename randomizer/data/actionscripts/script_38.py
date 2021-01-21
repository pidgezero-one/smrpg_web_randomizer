from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_38_sequence_looping_on_0',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_38_shadow_on_1',
        "command": 'shadow_on'
    },
    {
        "identifier": 'ACTION_38_set_priority_2',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_38_set_sprite_sequence_3',
        "command": 'set_sprite_sequence',
        "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_38_shift_east_pixels_4',
        "command": 'shift_east_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_38_face_southwest_5',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_38_start_loop_n_times_6',
        "command": 'start_loop_n_times',
        "args": [2]
    },
    {
        "identifier": 'ACTION_38_pause_7',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'ACTION_38_set_animation_speed_8',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_38_set_bit_9',
        "command": 'set_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'ACTION_38_shift_z_up_pixels_10',
        "command": 'shift_z_up_pixels',
        "args": [10]
    },
    {
        "identifier": 'ACTION_38_shift_z_down_pixels_11',
        "command": 'shift_z_down_pixels',
        "args": [10]
    },
    {
        "identifier": 'ACTION_38_pause_12',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'ACTION_38_end_loop_13',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_38_pause_14',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_38_set_bit_15',
        "command": 'set_bit',
        "args": [0x7043, 4]
    },
    {
        "identifier": 'ACTION_38_set_sprite_sequence_16',
        "command": 'set_sprite_sequence',
        "args": [3, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF]]
    },
    {
        "identifier": 'ACTION_38_pause_17',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'ACTION_38_set_animation_speed_18',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_38_fixed_f_coord_on_19',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_38_shift_west_steps_20',
        "command": 'shift_west_steps',
        "args": [4]
    },
    {
        "identifier": 'ACTION_38_set_animation_speed_21',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_38_shift_northwest_steps_22',
        "command": 'shift_northwest_steps',
        "args": [6]
    },
    {
        "identifier": 'ACTION_38_shift_north_steps_23',
        "command": 'shift_north_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_38_set_bit_24',
        "command": 'set_bit',
        "args": [0x7043, 4]
    },
    {
        "identifier": 'ACTION_38_set_sprite_sequence_25',
        "command": 'set_sprite_sequence',
        "args": [3, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF]]
    },
    {
        "identifier": 'ACTION_38_ret_26',
        "command": 'ret'
    }
]
