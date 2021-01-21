from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_439_object_memory_set_bit_0',
        "command": 'object_memory_set_bit',
        "args": [0x0d, [6]]
    },
    {
        "identifier": 'ACTION_439_pause_1',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_439_set_animation_speed_2',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_439_jmp_if_var_equals_byte_3',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70ae, 0, 'ACTION_439_visibility_off_57']
    },
    {
        "identifier": 'ACTION_439_bpl_26_27_28_4',
        "command": 'bpl_26_27_28'
    },
    {
        "identifier": 'ACTION_439_db_5',
        "command": 'db',
        "args": [0xc8, 0x87]
    },
    {
        "identifier": 'ACTION_439_set_short_6',
        "command": 'set_short',
        "args": [0x701a, 0x000c]
    },
    {
        "identifier": 'ACTION_439_db_7',
        "command": 'db',
        "args": [0x98]
    },
    {
        "identifier": 'ACTION_439_set_vram_priority_8',
        "command": 'set_vram_priority',
        "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
    },
    {
        "identifier": 'ACTION_439_set_priority_9',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_439_jmp_if_var_equals_byte_10',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70ae, 25, 'ACTION_439_db_19']
    },
    {
        "identifier": 'ACTION_439_db_11',
        "command": 'db',
        "args": [0x20, 0x04]
    },
    {
        "identifier": 'ACTION_439_embedded_animation_routine_12',
        "command": 'embedded_animation_routine',
        "args": [0x28]
    },
    {
        "identifier": 'ACTION_439_set_sprite_sequence_13',
        "command": 'set_sprite_sequence',
        "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_439_walk_to_xy_coords_14',
        "command": 'walk_to_xy_coords',
        "args": [3, 101]
    },
    {
        "identifier": 'ACTION_439_walk_to_xy_coords_15',
        "command": 'walk_to_xy_coords',
        "args": [8, 93]
    },
    {
        "identifier": 'ACTION_439_walk_to_xy_coords_16',
        "command": 'walk_to_xy_coords',
        "args": [14, 104]
    },
    {
        "identifier": 'ACTION_439_walk_to_xy_coords_17',
        "command": 'walk_to_xy_coords',
        "args": [8, 93]
    },
    {
        "identifier": 'ACTION_439_jmp_if_var_not_equals_byte_18',
        "command": 'jmp_if_var_not_equals_byte',
        "args": [0x70ae, 25, 'ACTION_439_walk_to_xy_coords_14']
    },
    {
        "identifier": 'ACTION_439_db_19',
        "command": 'db',
        "args": [0xc8, 0x80]
    },
    {
        "identifier": 'ACTION_439_run_away_shift_20',
        "command": 'run_away_shift'
    },
    {
        "identifier": 'ACTION_439_bpl_26_27_28_21',
        "command": 'bpl_26_27_28'
    },
    {
        "identifier": 'ACTION_439_reset_properties_22',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_439_fixed_f_coord_off_23',
        "command": 'fixed_f_coord_off'
    },
    {
        "identifier": 'ACTION_439_face_mario_24',
        "command": 'face_mario'
    },
    {
        "identifier": 'ACTION_439_set_700C_to_object_coord_25',
        "command": 'set_700C_to_object_coord',
        "args": [AreaObjects.DUMMY_0X07, Coords.F]
    },
    {
        "identifier": 'ACTION_439_add_26',
        "command": 'add',
        "args": [0x700c, 0x01]
    },
    {
        "identifier": 'ACTION_439_mem_700C_and_const_27',
        "command": 'mem_700C_and_const',
        "args": [0x0007]
    },
    {
        "identifier": 'ACTION_439_mem_compare_28',
        "command": 'mem_compare',
        "args": [0x700c, 4]
    },
    {
        "identifier": 'ACTION_439_jmp_if_comparison_result_is_greater_or_equal_29',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['ACTION_439_set_animation_speed_44']
    },
    {
        "identifier": 'ACTION_439_set_animation_speed_30',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_439_face_southeast_31',
        "command": 'face_southeast'
    },
    {
        "identifier": 'ACTION_439_set_sprite_sequence_32',
        "command": 'set_sprite_sequence',
        "args": [3, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_439_db_33',
        "command": 'db',
        "args": [0xc7, 0x07]
    },
    {
        "identifier": 'ACTION_439_set_bit_34',
        "command": 'set_bit',
        "args": [0x7044, 7]
    },
    {
        "identifier": 'ACTION_439_pause_35',
        "command": 'pause',
        "args": [48]
    },
    {
        "identifier": 'ACTION_439_db_36',
        "command": 'db',
        "args": [0xfd, 0x3e, 0x1c, 0x05, 0x0c, 0x89, 0x54]
    },
    {
        "identifier": 'ACTION_439_reset_properties_37',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_439_set_animation_speed_38',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_439_pause_39',
        "command": 'pause',
        "args": [128]
    },
    {
        "identifier": 'ACTION_439_set_animation_speed_40',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_439_walk_to_xy_coords_41',
        "command": 'walk_to_xy_coords',
        "args": [18, 73]
    },
    {
        "identifier": 'ACTION_439_visibility_off_42',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_439_ret_43',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_439_set_animation_speed_44',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_439_face_southwest_45',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_439_set_sprite_sequence_46',
        "command": 'set_sprite_sequence',
        "args": [3, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF]]
    },
    {
        "identifier": 'ACTION_439_db_47',
        "command": 'db',
        "args": [0xc7, 0x07]
    },
    {
        "identifier": 'ACTION_439_pause_48',
        "command": 'pause',
        "args": [48]
    },
    {
        "identifier": 'ACTION_439_db_49',
        "command": 'db',
        "args": [0xfd, 0x3e, 0x1c, 0x05, 0x0c, 0xa6, 0x54]
    },
    {
        "identifier": 'ACTION_439_reset_properties_50',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_439_set_animation_speed_51',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_439_pause_52',
        "command": 'pause',
        "args": [128]
    },
    {
        "identifier": 'ACTION_439_set_animation_speed_53',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_439_walk_to_xy_coords_54',
        "command": 'walk_to_xy_coords',
        "args": [0, 73]
    },
    {
        "identifier": 'ACTION_439_visibility_off_55',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_439_ret_56',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_439_visibility_off_57',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_439_object_memory_set_bit_58',
        "command": 'object_memory_set_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_439_ret_59',
        "command": 'ret'
    }
]
