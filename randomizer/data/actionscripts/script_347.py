from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_347_visibility_off_0',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_347_set_sprite_sequence_1',
        "command": 'set_sprite_sequence',
        "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_347_transfer_to_object_xy_2',
        "command": 'transfer_to_object_xy',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'ACTION_347_transfer_xyzf_pixels_3',
        "command": 'transfer_xyzf_pixels',
        "args": [0, 0, 8, RadialDirections.NORTHEAST]
    },
    {
        "identifier": 'ACTION_347_jmp_if_var_equals_short_4',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7032, 1, 'ACTION_347_pause_13']
    },
    {
        "identifier": 'ACTION_347_pause_5',
        "command": 'pause',
        "args": [7]
    },
    {
        "identifier": 'ACTION_347_visibility_on_6',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_347_set_animation_speed_7',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_347_shift_z_up_pixels_8',
        "command": 'shift_z_up_pixels',
        "args": [4]
    },
    {
        "identifier": 'ACTION_347_set_animation_speed_9',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_347_shift_z_up_pixels_10',
        "command": 'shift_z_up_pixels',
        "args": [6]
    },
    {
        "identifier": 'ACTION_347_visibility_off_11',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_347_ret_12',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_347_pause_13',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_347_jmp_if_var_not_equals_short_14',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7032, 1, 'ACTION_347_pause_13']
    },
    {
        "identifier": 'ACTION_347_transfer_to_object_xy_15',
        "command": 'transfer_to_object_xy',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'ACTION_347_transfer_xyzf_pixels_16',
        "command": 'transfer_xyzf_pixels',
        "args": [0, 0, 8, RadialDirections.NORTHEAST]
    },
    {
        "identifier": 'ACTION_347_visibility_on_17',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_347_pause_18',
        "command": 'pause',
        "args": [42]
    },
    {
        "identifier": 'ACTION_347_set_animation_speed_19',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_347_shift_z_up_steps_20',
        "command": 'shift_z_up_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_347_shift_z_up_pixels_21',
        "command": 'shift_z_up_pixels',
        "args": [2]
    },
    {
        "identifier": 'ACTION_347_set_animation_speed_22',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_347_shift_z_up_pixels_23',
        "command": 'shift_z_up_pixels',
        "args": [6]
    },
    {
        "identifier": 'ACTION_347_set_animation_speed_24',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_347_shift_z_up_pixels_25',
        "command": 'shift_z_up_pixels',
        "args": [4]
    },
    {
        "identifier": 'ACTION_347_pause_26',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_347_jmp_if_var_not_equals_short_27',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7032, 2, 'ACTION_347_pause_26']
    },
    {
        "identifier": 'ACTION_347_set_animation_speed_28',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_347_shift_z_up_steps_29',
        "command": 'shift_z_up_steps',
        "args": [8]
    },
    {
        "identifier": 'ACTION_347_visibility_off_30',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_347_ret_31',
        "command": 'ret'
    }
]
