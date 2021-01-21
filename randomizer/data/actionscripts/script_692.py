from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_692_db_0',
        "command": 'db',
        "args": [0xfd, 0x12]
    },
    {
        "identifier": 'ACTION_692_set_sprite_sequence_1',
        "command": 'set_sprite_sequence',
        "args": [5, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_692_pause_2',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'ACTION_692_set_animation_speed_3',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_692_db_4',
        "command": 'db',
        "args": [0x20, 0x07]
    },
    {
        "identifier": 'ACTION_692_db_5',
        "command": 'db',
        "args": [0x24, 0x50, 0xff, 0xa8, 0x00]
    },
    {
        "identifier": 'ACTION_692_db_6',
        "command": 'db',
        "args": [0x25, 0x00, 0x08, 0x80, 0xff]
    },
    {
        "identifier": 'ACTION_692_pause_7',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'ACTION_692_bpl_26_27_28_8',
        "command": 'bpl_26_27_28'
    },
    {
        "identifier": 'ACTION_692_set_animation_speed_9',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_692_set_sprite_sequence_10',
        "command": 'set_sprite_sequence',
        "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_692_pause_11',
        "command": 'pause',
        "args": [96]
    },
    {
        "identifier": 'ACTION_692_set_sprite_sequence_12',
        "command": 'set_sprite_sequence',
        "args": [5, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_692_set_animation_speed_13',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_692_db_14',
        "command": 'db',
        "args": [0x20, 0x07]
    },
    {
        "identifier": 'ACTION_692_db_15',
        "command": 'db',
        "args": [0x24, 0xb0, 0x00, 0x58, 0xff]
    },
    {
        "identifier": 'ACTION_692_db_16',
        "command": 'db',
        "args": [0x25, 0xc0, 0x06, 0x80, 0xff]
    },
    {
        "identifier": 'ACTION_692_pause_17',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'ACTION_692_bpl_26_27_28_18',
        "command": 'bpl_26_27_28'
    },
    {
        "identifier": 'ACTION_692_face_southwest_19',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_692_reset_properties_20',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_692_set_animation_speed_21',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_692_sequence_looping_on_22',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_692_pause_23',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'ACTION_692_set_700C_to_pressed_button_24',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_692_jmp_if_var_equals_short_25',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 20, 'ACTION_692_set_700C_to_object_coord_30']
    },
    {
        "identifier": 'ACTION_692_jmp_if_var_equals_short_26',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 21, 'ACTION_692_set_700C_to_object_coord_37']
    },
    {
        "identifier": 'ACTION_692_jmp_if_var_equals_short_27',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 22, 'ACTION_692_set_700C_to_object_coord_44']
    },
    {
        "identifier": 'ACTION_692_jmp_if_var_equals_short_28',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 23, 'ACTION_692_set_700C_to_object_coord_51']
    },
    {
        "identifier": 'ACTION_692_ret_29',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_692_set_700C_to_object_coord_30',
        "command": 'set_700C_to_object_coord',
        "args": [AreaObjects.NPC_0, Coords.Z, CoordUnits.PIXEL]
    },
    {
        "identifier": 'ACTION_692_jmp_if_var_equals_short_31',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 0, 'ACTION_692_clear_bit_34']
    },
    {
        "identifier": 'ACTION_692_walk_to_xy_coords_32',
        "command": 'walk_to_xy_coords',
        "args": [7, 115]
    },
    {
        "identifier": 'ACTION_692_face_southwest_33',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_692_clear_bit_34',
        "command": 'clear_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'ACTION_692_transfer_to_xyzf_35',
        "command": 'transfer_to_xyzf',
        "args": [7, 115, 4, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_692_ret_36',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_692_set_700C_to_object_coord_37',
        "command": 'set_700C_to_object_coord',
        "args": [AreaObjects.NPC_1, Coords.Z, CoordUnits.PIXEL]
    },
    {
        "identifier": 'ACTION_692_jmp_if_var_equals_short_38',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 0, 'ACTION_692_clear_bit_41']
    },
    {
        "identifier": 'ACTION_692_walk_to_xy_coords_39',
        "command": 'walk_to_xy_coords',
        "args": [8, 107]
    },
    {
        "identifier": 'ACTION_692_face_southwest_40',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_692_clear_bit_41',
        "command": 'clear_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'ACTION_692_transfer_to_xyzf_42',
        "command": 'transfer_to_xyzf',
        "args": [8, 107, 4, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_692_ret_43',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_692_set_700C_to_object_coord_44',
        "command": 'set_700C_to_object_coord',
        "args": [AreaObjects.NPC_2, Coords.Z, CoordUnits.PIXEL]
    },
    {
        "identifier": 'ACTION_692_jmp_if_var_equals_short_45',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 0, 'ACTION_692_clear_bit_48']
    },
    {
        "identifier": 'ACTION_692_walk_to_xy_coords_46',
        "command": 'walk_to_xy_coords',
        "args": [12, 107]
    },
    {
        "identifier": 'ACTION_692_face_southwest_47',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_692_clear_bit_48',
        "command": 'clear_bit',
        "args": [0x7043, 2]
    },
    {
        "identifier": 'ACTION_692_transfer_to_xyzf_49',
        "command": 'transfer_to_xyzf',
        "args": [12, 107, 4, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_692_ret_50',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_692_set_700C_to_object_coord_51',
        "command": 'set_700C_to_object_coord',
        "args": [AreaObjects.NPC_3, Coords.Z, CoordUnits.PIXEL]
    },
    {
        "identifier": 'ACTION_692_jmp_if_var_equals_short_52',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 8, 'ACTION_692_clear_bit_55']
    },
    {
        "identifier": 'ACTION_692_walk_to_xy_coords_53',
        "command": 'walk_to_xy_coords',
        "args": [11, 95]
    },
    {
        "identifier": 'ACTION_692_face_southwest_54',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_692_clear_bit_55',
        "command": 'clear_bit',
        "args": [0x7043, 3]
    },
    {
        "identifier": 'ACTION_692_transfer_to_xyzf_56',
        "command": 'transfer_to_xyzf',
        "args": [11, 95, 8, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_692_ret_57',
        "command": 'ret'
    }
]
