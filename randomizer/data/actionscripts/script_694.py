from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_694_db_0',
        "command": 'db',
        "args": [0xfd, 0x12]
    },
    {
        "identifier": 'ACTION_694_floating_off_1',
        "command": 'floating_off'
    },
    {
        "identifier": 'ACTION_694_set_sprite_sequence_2',
        "command": 'set_sprite_sequence',
        "args": [5, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_694_pause_3',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'ACTION_694_set_animation_speed_4',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_694_db_5',
        "command": 'db',
        "args": [0x20, 0x07]
    },
    {
        "identifier": 'ACTION_694_db_6',
        "command": 'db',
        "args": [0x24, 0xc0, 0x00, 0xc0, 0xff]
    },
    {
        "identifier": 'ACTION_694_db_7',
        "command": 'db',
        "args": [0x25, 0x00, 0x08, 0x80, 0xff]
    },
    {
        "identifier": 'ACTION_694_pause_8',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'ACTION_694_bpl_26_27_28_9',
        "command": 'bpl_26_27_28'
    },
    {
        "identifier": 'ACTION_694_set_animation_speed_10',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_694_set_sprite_sequence_11',
        "command": 'set_sprite_sequence',
        "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_694_pause_12',
        "command": 'pause',
        "args": [96]
    },
    {
        "identifier": 'ACTION_694_set_sprite_sequence_13',
        "command": 'set_sprite_sequence',
        "args": [5, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_694_set_animation_speed_14',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_694_db_15',
        "command": 'db',
        "args": [0x20, 0x07]
    },
    {
        "identifier": 'ACTION_694_db_16',
        "command": 'db',
        "args": [0x24, 0x40, 0xff, 0x40, 0x00]
    },
    {
        "identifier": 'ACTION_694_db_17',
        "command": 'db',
        "args": [0x25, 0xc0, 0x06, 0x80, 0xff]
    },
    {
        "identifier": 'ACTION_694_pause_18',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'ACTION_694_bpl_26_27_28_19',
        "command": 'bpl_26_27_28'
    },
    {
        "identifier": 'ACTION_694_face_southwest_20',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_694_reset_properties_21',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_694_set_animation_speed_22',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_694_sequence_looping_on_23',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_694_pause_24',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'ACTION_694_set_700C_to_pressed_button_25',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_694_jmp_if_700C_equals_short_26',
        "command": 'jmp_if_700C_equals_short',
        "args": [20, 'ACTION_694_set_700C_to_object_coord_31']
    },
    {
        "identifier": 'ACTION_694_jmp_if_700C_equals_short_27',
        "command": 'jmp_if_700C_equals_short',
        "args": [21, 'ACTION_694_set_700C_to_object_coord_38']
    },
    {
        "identifier": 'ACTION_694_jmp_if_700C_equals_short_28',
        "command": 'jmp_if_700C_equals_short',
        "args": [22, 'ACTION_694_set_700C_to_object_coord_45']
    },
    {
        "identifier": 'ACTION_694_jmp_if_700C_equals_short_29',
        "command": 'jmp_if_700C_equals_short',
        "args": [23, 'ACTION_694_set_700C_to_object_coord_52']
    },
    {
        "identifier": 'ACTION_694_ret_30',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_694_set_700C_to_object_coord_31',
        "command": 'set_700C_to_object_coord',
        "args": [AreaObjects.NPC_0, Coords.Z, [7], CoordUnits.PIXEL]
    },
    {
        "identifier": 'ACTION_694_jmp_if_700C_equals_short_32',
        "command": 'jmp_if_700C_equals_short',
        "args": [0, 'ACTION_694_clear_bit_35']
    },
    {
        "identifier": 'ACTION_694_walk_to_xy_coords_33',
        "command": 'walk_to_xy_coords',
        "args": [7, 115]
    },
    {
        "identifier": 'ACTION_694_face_southwest_34',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_694_clear_bit_35',
        "command": 'clear_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'ACTION_694_transfer_to_xyzf_36',
        "command": 'transfer_to_xyzf',
        "args": [7, 115, 4, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_694_ret_37',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_694_set_700C_to_object_coord_38',
        "command": 'set_700C_to_object_coord',
        "args": [AreaObjects.NPC_1, Coords.Z, [7], CoordUnits.PIXEL]
    },
    {
        "identifier": 'ACTION_694_jmp_if_700C_equals_short_39',
        "command": 'jmp_if_700C_equals_short',
        "args": [0, 'ACTION_694_clear_bit_42']
    },
    {
        "identifier": 'ACTION_694_walk_to_xy_coords_40',
        "command": 'walk_to_xy_coords',
        "args": [8, 107]
    },
    {
        "identifier": 'ACTION_694_face_southwest_41',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_694_clear_bit_42',
        "command": 'clear_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'ACTION_694_transfer_to_xyzf_43',
        "command": 'transfer_to_xyzf',
        "args": [8, 107, 4, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_694_ret_44',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_694_set_700C_to_object_coord_45',
        "command": 'set_700C_to_object_coord',
        "args": [AreaObjects.NPC_2, Coords.Z, [7], CoordUnits.PIXEL]
    },
    {
        "identifier": 'ACTION_694_jmp_if_700C_equals_short_46',
        "command": 'jmp_if_700C_equals_short',
        "args": [0, 'ACTION_694_clear_bit_49']
    },
    {
        "identifier": 'ACTION_694_walk_to_xy_coords_47',
        "command": 'walk_to_xy_coords',
        "args": [12, 107]
    },
    {
        "identifier": 'ACTION_694_face_southwest_48',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_694_clear_bit_49',
        "command": 'clear_bit',
        "args": [0x7043, 2]
    },
    {
        "identifier": 'ACTION_694_transfer_to_xyzf_50',
        "command": 'transfer_to_xyzf',
        "args": [12, 107, 4, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_694_ret_51',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_694_set_700C_to_object_coord_52',
        "command": 'set_700C_to_object_coord',
        "args": [AreaObjects.NPC_3, Coords.Z, [7], CoordUnits.PIXEL]
    },
    {
        "identifier": 'ACTION_694_jmp_if_700C_equals_short_53',
        "command": 'jmp_if_700C_equals_short',
        "args": [8, 'ACTION_694_clear_bit_56']
    },
    {
        "identifier": 'ACTION_694_walk_to_xy_coords_54',
        "command": 'walk_to_xy_coords',
        "args": [11, 95]
    },
    {
        "identifier": 'ACTION_694_face_southwest_55',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_694_clear_bit_56',
        "command": 'clear_bit',
        "args": [0x7043, 3]
    },
    {
        "identifier": 'ACTION_694_transfer_to_xyzf_57',
        "command": 'transfer_to_xyzf',
        "args": [11, 95, 8, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_694_ret_58',
        "command": 'ret'
    }
]
