from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_664_transfer_to_xyzf_0',
        "command": 'transfer_to_xyzf',
        "args": [15, 55, 2, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_664_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_664_set_animation_speed_2',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_664_visibility_on_3',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_664_clear_solidity_bits_4',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_664_clear_solidity_bits_5',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_664_set_bit_6',
        "command": 'set_bit',
        "args": [0x7060, 1]
    },
    {
        "identifier": 'ACTION_664_walk_1_step_southeast_7',
        "command": 'walk_1_step_southeast'
    },
    {
        "identifier": 'ACTION_664_face_northwest_8',
        "command": 'face_northwest'
    },
    {
        "identifier": 'ACTION_664_pause_9',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'ACTION_664_set_solidity_bits_10',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_664_shift_southeast_steps_11',
        "command": 'shift_southeast_steps',
        "args": [4]
    },
    {
        "identifier": 'ACTION_664_set_solidity_bits_12',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_664_floating_on_13',
        "command": 'floating_on'
    },
    {
        "identifier": 'ACTION_664_shift_southwest_steps_14',
        "command": 'shift_southwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_664_clear_solidity_bits_15',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_664_floating_off_16',
        "command": 'floating_off'
    },
    {
        "identifier": 'ACTION_664_shift_southwest_steps_17',
        "command": 'shift_southwest_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_664_face_northwest_18',
        "command": 'face_northwest'
    },
    {
        "identifier": 'ACTION_664_pause_19',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'ACTION_664_walk_1_step_northeast_20',
        "command": 'walk_1_step_northeast'
    },
    {
        "identifier": 'ACTION_664_face_northwest_21',
        "command": 'face_northwest'
    },
    {
        "identifier": 'ACTION_664_fixed_f_coord_on_22',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_664_start_loop_n_times_23',
        "command": 'start_loop_n_times',
        "args": [2]
    },
    {
        "identifier": 'ACTION_664_set_animation_speed_24',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_664_shift_z_up_pixels_25',
        "command": 'shift_z_up_pixels',
        "args": [6]
    },
    {
        "identifier": 'ACTION_664_set_animation_speed_26',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_664_shift_z_down_pixels_27',
        "command": 'shift_z_down_pixels',
        "args": [6]
    },
    {
        "identifier": 'ACTION_664_pause_28',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_664_end_loop_29',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_664_fixed_f_coord_off_30',
        "command": 'fixed_f_coord_off'
    },
    {
        "identifier": 'ACTION_664_set_animation_speed_31',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_664_walk_1_step_southwest_32',
        "command": 'walk_1_step_southwest'
    },
    {
        "identifier": 'ACTION_664_face_northwest_33',
        "command": 'face_northwest'
    },
    {
        "identifier": 'ACTION_664_pause_34',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'ACTION_664_set_animation_speed_35',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_664_shift_northeast_steps_36',
        "command": 'shift_northeast_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_664_set_solidity_bits_37',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_664_floating_on_38',
        "command": 'floating_on'
    },
    {
        "identifier": 'ACTION_664_shift_northeast_steps_39',
        "command": 'shift_northeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_664_clear_solidity_bits_40',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_664_floating_off_41',
        "command": 'floating_off'
    },
    {
        "identifier": 'ACTION_664_shift_northwest_steps_42',
        "command": 'shift_northwest_steps',
        "args": [4]
    },
    {
        "identifier": 'ACTION_664_pause_43',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_664_clear_bit_44',
        "command": 'clear_bit',
        "args": [0x7060, 1]
    },
    {
        "identifier": 'ACTION_664_clear_solidity_bits_45',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_664_walk_1_step_northwest_46',
        "command": 'walk_1_step_northwest'
    },
    {
        "identifier": 'ACTION_664_visibility_off_47',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_664_transfer_to_xyzf_48',
        "command": 'transfer_to_xyzf',
        "args": [22, 77, 0, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_664_ret_49',
        "command": 'ret'
    }
]
