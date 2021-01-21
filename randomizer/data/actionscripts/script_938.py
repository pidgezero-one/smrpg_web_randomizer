from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_938_set_sprite_sequence_0',
        "command": 'set_sprite_sequence',
        "args": [5, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_938_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_938_shift_south_steps_2',
        "command": 'shift_south_steps',
        "args": [4]
    },
    {
        "identifier": 'ACTION_938_shift_south_pixels_3',
        "command": 'shift_south_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_938_set_bit_4',
        "command": 'set_bit',
        "args": [0x7044, 7]
    },
    {
        "identifier": 'ACTION_938_start_loop_n_times_5',
        "command": 'start_loop_n_times',
        "args": [4]
    },
    {
        "identifier": 'ACTION_938_shift_north_pixels_6',
        "command": 'shift_north_pixels',
        "args": [4]
    },
    {
        "identifier": 'ACTION_938_shift_south_pixels_7',
        "command": 'shift_south_pixels',
        "args": [4]
    },
    {
        "identifier": 'ACTION_938_end_loop_8',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_938_set_sprite_sequence_9',
        "command": 'set_sprite_sequence',
        "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_938_jump_to_height_silent_10',
        "command": 'jump_to_height_silent',
        "args": [256]
    },
    {
        "identifier": 'ACTION_938_pause_11',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'ACTION_938_set_bit_12',
        "command": 'set_bit',
        "args": [0x7043, 6]
    },
    {
        "identifier": 'ACTION_938_ret_13',
        "command": 'ret'
    }
]
