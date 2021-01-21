from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_802_face_southwest_0',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_802_fixed_f_coord_on_1',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_802_sequence_looping_on_2',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_802_jmp_if_random_above_128_3',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_802_fixed_f_coord_off_18']
    },
    {
        "identifier": 'ACTION_802_shift_northeast_pixels_4',
        "command": 'shift_northeast_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_802_sequence_looping_off_5',
        "command": 'sequence_looping_off'
    },
    {
        "identifier": 'ACTION_802_set_sprite_sequence_6',
        "command": 'set_sprite_sequence',
        "args": [9, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_802_pause_7',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'ACTION_802_set_animation_speed_8',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_802_shift_southwest_pixels_9',
        "command": 'shift_southwest_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_802_set_sprite_sequence_10',
        "command": 'set_sprite_sequence',
        "args": [1, inc_sprite=3, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_802_pause_11',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_802_reset_properties_12',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_802_set_animation_speed_13',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_802_pause_14',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'ACTION_802_set_sprite_sequence_15',
        "command": 'set_sprite_sequence',
        "args": [8, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_802_pause_16',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_802_reset_properties_17',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_802_fixed_f_coord_off_18',
        "command": 'fixed_f_coord_off'
    },
    {
        "identifier": 'ACTION_802_walk_1_step_east_19',
        "command": 'walk_1_step_east'
    },
    {
        "identifier": 'ACTION_802_walk_1_step_north_20',
        "command": 'walk_1_step_north'
    },
    {
        "identifier": 'ACTION_802_clear_solidity_bits_21',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_802_shift_northeast_steps_22',
        "command": 'shift_northeast_steps',
        "args": [4]
    },
    {
        "identifier": 'ACTION_802_shift_northeast_pixels_23',
        "command": 'shift_northeast_pixels',
        "args": [4]
    },
    {
        "identifier": 'ACTION_802_shift_northwest_steps_24',
        "command": 'shift_northwest_steps',
        "args": [4]
    },
    {
        "identifier": 'ACTION_802_sequence_looping_off_25',
        "command": 'sequence_looping_off'
    },
    {
        "identifier": 'ACTION_802_face_southwest_26',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_802_set_solidity_bits_27',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_802_ret_28',
        "command": 'ret'
    }
]
