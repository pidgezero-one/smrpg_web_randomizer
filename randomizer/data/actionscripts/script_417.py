from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_417_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_417_visibility_off_1',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_417_transfer_to_xyzf_2',
        "command": 'transfer_to_xyzf',
        "args": [5, 115, 1, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_417_jmp_if_bit_clear_3',
        "command": 'jmp_if_bit_clear',
        "args": [0x7049, 6, 'ACTION_417_set_700C_to_pressed_button_5']
    },
    {
        "identifier": 'ACTION_417_set_animation_speed_4',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_417_set_700C_to_pressed_button_5',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_417_mem_compare_val_6',
        "command": 'mem_compare_val',
        "args": [25]
    },
    {
        "identifier": 'ACTION_417_jmp_if_comparison_result_is_lesser_7',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['ACTION_417_shift_z_up_pixels_16']
    },
    {
        "identifier": 'ACTION_417_mem_compare_val_8',
        "command": 'mem_compare_val',
        "args": [29]
    },
    {
        "identifier": 'ACTION_417_jmp_if_comparison_result_is_greater_or_equal_9',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['ACTION_417_jmp_if_bit_set_28']
    },
    {
        "identifier": 'ACTION_417_jmp_if_bit_set_10',
        "command": 'jmp_if_bit_set',
        "args": [0x7049, 6, 'ACTION_417_set_animation_speed_14']
    },
    {
        "identifier": 'ACTION_417_set_animation_speed_11',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_417_pause_12',
        "command": 'pause',
        "args": [6]
    },
    {
        "identifier": 'ACTION_417_jmp_13',
        "command": 'jmp',
        "args": ['ACTION_417_shift_z_up_pixels_16']
    },
    {
        "identifier": 'ACTION_417_set_animation_speed_14',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_417_pause_15',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'ACTION_417_shift_z_up_pixels_16',
        "command": 'shift_z_up_pixels',
        "args": [6]
    },
    {
        "identifier": 'ACTION_417_reset_properties_17',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_417_visibility_on_18',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_417_shift_z_up_pixels_19',
        "command": 'shift_z_up_pixels',
        "args": [10]
    },
    {
        "identifier": 'ACTION_417_set_solidity_bits_20',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_417_pause_21',
        "command": 'pause',
        "args": [40]
    },
    {
        "identifier": 'ACTION_417_clear_solidity_bits_22',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_417_pause_23',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'ACTION_417_shift_z_down_pixels_24',
        "command": 'shift_z_down_pixels',
        "args": [10]
    },
    {
        "identifier": 'ACTION_417_visibility_off_25',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_417_bounce_to_xy_with_height_26',
        "command": 'bounce_to_xy_with_height',
        "args": [5, 115, 1]
    },
    {
        "identifier": 'ACTION_417_jmp_27',
        "command": 'jmp',
        "args": ['ACTION_417_transfer_to_xyzf_47']
    },
    {
        "identifier": 'ACTION_417_jmp_if_bit_set_28',
        "command": 'jmp_if_bit_set',
        "args": [0x7049, 6, 'ACTION_417_pause_30']
    },
    {
        "identifier": 'ACTION_417_pause_29',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_417_pause_30',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_417_transfer_xyzf_pixels_31',
        "command": 'transfer_xyzf_pixels',
        "args": [254, 0, 0, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_417_shift_z_up_pixels_32',
        "command": 'shift_z_up_pixels',
        "args": [4]
    },
    {
        "identifier": 'ACTION_417_reset_properties_33',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_417_visibility_on_34',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_417_shift_z_up_pixels_35',
        "command": 'shift_z_up_pixels',
        "args": [10]
    },
    {
        "identifier": 'ACTION_417_set_solidity_bits_36',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_417_pause_37',
        "command": 'pause',
        "args": [28]
    },
    {
        "identifier": 'ACTION_417_clear_solidity_bits_38',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_417_pause_39',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_417_shift_z_down_pixels_40',
        "command": 'shift_z_down_pixels',
        "args": [10]
    },
    {
        "identifier": 'ACTION_417_visibility_off_41',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_417_bounce_to_xy_with_height_42',
        "command": 'bounce_to_xy_with_height',
        "args": [5, 115, 1]
    },
    {
        "identifier": 'ACTION_417_jmp_if_bit_set_43',
        "command": 'jmp_if_bit_set',
        "args": [0x7049, 6, 'ACTION_417_pause_45']
    },
    {
        "identifier": 'ACTION_417_pause_44',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_417_pause_45',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_417_jmp_46',
        "command": 'jmp',
        "args": ['ACTION_417_transfer_to_xyzf_47']
    },
    {
        "identifier": 'ACTION_417_transfer_to_xyzf_47',
        "command": 'transfer_to_xyzf',
        "args": [8, 60, 0, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_417_clear_bit_48',
        "command": 'clear_bit',
        "args": [0x7044, 1]
    },
    {
        "identifier": 'ACTION_417_ret_49',
        "command": 'ret'
    }
]
